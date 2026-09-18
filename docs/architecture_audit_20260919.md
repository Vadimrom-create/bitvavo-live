# Audit contradictoire de l'architecture de décision — 2026-09-19

## Objet

Question centrale : lorsqu'un marché Bitvavo commence un mouvement réellement exploitable, par quelles étapes passe-t-il avant une alerte ACHÈTE, et à quelle étape peut-il être perdu, retardé ou mal classé ?

Cet audit distingue :
- bugs / incohérences certaines ;
- choix d'architecture qui dégradent la couverture ou la latence ;
- contraintes réelles de Bitvavo ;
- limites de preuve historique.

Il ne modifie pas les coefficients ni les seuils de V4 gelée.

## Conclusion exécutive

Le problème principal n'est pas un mauvais coefficient. Le pipeline mélange aujourd'hui :
1. un collecteur legacy servant réellement à V4 ;
2. une collecte full-universe plus propre effectuée après la décision ;
3. des contrôles qualité globaux qui peuvent invalider une opportunité pour un trou de bougie correspondant à zéro trade ;
4. une couche Decision Layer / accélération qui est mieux adaptée à certaines erreurs observées mais reste shadow ;
5. GitHub Actions utilisé comme horloge de trading alors que sa cadence réelle est très supérieure à 5 minutes.

Le système contient de bonnes protections de sécurité/replay, mais le chemin causal de détection -> décision -> alerte reste trop indirect et trop fragile.

## P0 — Bloqueurs absolus

### P0.1 Cache journalier V4 faussement frais

Avant correction :
- 414 profils présents ;
- 414/414 vieux de plus de 3 h ;
- 412/414 vieux de plus de 72 h ;
- 402/414 vieux de plus de 7 jours ;
- pourtant le cache global affichait un timestamp courant.

Cause : v4_common.refresh_trend_cache() gère une TTL globale. Une mise à jour d'un petit sous-ensemble de marchés remet le timestamp global à maintenant, laissant les autres profils périmés.

Impact : un BUY_READY reçoit STALE_DAILY_PROFILE si son profil dépasse 3 h. HYPE-EUR a effectivement été stabilisé BUY_READY puis bloqué par ce veto.

Correction appliquée :
- research/trend_cache_guard.py ;
- fraîcheur vérifiée par marché avant V4 ;
- rafraîchissement des profils périmés ;
- audit trend_cache_guard.json ;
- tests de non-régression ;
- scoring V4 inchangé.

### P0.2 La collecte full-universe durcie n'alimente pas V4

Ordre actuel :
collector-2 legacy -> V3/V4 -> adaptive entry -> stabilizer -> ensuite seulement collecte 427 marchés en bougies closes 5m/15m -> qualité / journal / évaluation.

Impact : la donnée la plus robuste sert à contrôler une décision déjà prise, pas à produire cette décision.

Le collecteur legacy :
- filtre volume >= 5 000 EUR/24h ;
- utilise un résumé 15m legacy ;
- peut intégrer la bougie en formation ;
- n'enrichit en 1h/4h qu'un sous-ensemble ;
- carnet seulement pour un sous-ensemble.

Correctif cible : une seule source canonique de données en amont du moteur de décision.

### P0.3 Cadence réelle incompatible avec un radar court terme

Mesure sur 39 intervalles récents entre rapports publiés :
- médiane ~14.9 min ;
- 36/39 > 10 min ;
- 19/39 > 15 min ;
- maximum ~20.4 min.

Impact : un mouvement qui naît entre deux publications peut être détecté après une grande partie de son impulsion.

Correctif cible : sortir le radar temps réel de GitHub Actions. GitHub doit devenir audit/replay/release, pas l'horloge de trading.

## P1 — Fortes sources de faux négatifs

### P1.1 Toute lacune de bougie invalide la série

Le validateur considère actuellement tout CANDLE_GAPS comme invalidant.

Bitvavo ne produit pas de bougie quand aucun trade n'a lieu dans l'intervalle. L'absence d'une bougie n'implique donc pas automatiquement une perte de données.

Snapshot :
- 427 marchés ;
- 27 valides 5m ;
- 78 valides 15m ;
- 26 valides simultanément ;
- 400 INVALID_5M ;
- 349 INVALID_15M.

Même parmi les marchés >= 250k EUR/24h :
- 96 marchés ;
- seulement 24 strategy-grade ;
- plusieurs gros movers sont exclus pour 1 à 3 intervalles sans bougie.

Exemples :
- C-EUR +28.5 %, 1 trou 5m ;
- RAY-EUR +21.3 %, 2 trous 5m ;
- OP-EUR +17.2 %, 3 trous 5m ;
- EPIC-EUR +18.7 %, 1 trou 15m ;
- UNI-EUR +14.7 %, ~6.3M EUR de volume, 3 trous 5m.

Correctif cible :
- reconstruire une grille temporelle explicite ;
- différencier NO_TRADE_INTERVAL et MISSING_DATA ;
- pour NO_TRADE_INTERVAL, barre marquée no_trade=true, OHLC=close précédent, volume=0 ;
- utiliser une métrique de sparsité/liquidité séparée comme veto d'exécution ;
- ne jamais inventer un trade.

### P1.2 Présélection / enrichissement historique trop bornés

V4 gelée : ENTRY_ENRICH_COUNT=72. Un marché non retenu recevait NOT_ENTRY_ENRICHED.

Correction opérationnelle déjà appliquée :
- 72 enrichissements de base ;
- jusqu'à 24 promotions adaptatives same-cycle ;
- critères : watch persistante, mover émergent, accélération, volume, rank surge ;
- total jusqu'à 96 ;
- scoring et seuils V4 inchangés.

Cette correction a déjà transformé des "NOT_ENTRY_ENRICHED" en vraies décisions (ex. F/ARB/C).

### P1.3 Decision Layer et accélération ne participent pas à l'alerte

Le code indique explicitement :
- Decision Layer = shadow ;
- acceleration = shadow ;
- candidate memory = shadow ;
- alert_integration=false.

Impact : ces couches peuvent identifier une anomalie ou une structure intéressante, mais la voie opérationnelle d'achat reste V4 buy_ready + qualité + risque.

Correctif cible : après évaluation/versioning, faire de la Decision Layer un arbitre opérationnel des candidats qualifiés, sans laisser une métrique de timing effacer silencieusement une structure forte.

### P1.4 Données de scoring et données de validation n'ont pas la même sémantique

Le collecteur legacy résume la dernière bougie retournée sans filtre explicite de bougie close. Le pipeline full-universe, lui, utilise closed_candles().

Impact :
- scoring potentiellement fondé sur une bougie en formation ;
- validation fondée sur une bougie close ;
- contradictions et bruit ;
- stabilizer utilisé en partie pour compenser des oscillations venant de la source.

Correctif cible : constructeur de barres unique ; features closed-bar et live-partial séparées explicitement.

## P1 — Preuves de faux négatifs historiques

Le contrôle des movers montre :
- F +67 % : NOT_DETECTED / DATA ;
- G +56.9 % : NOT_DETECTED / DATA ;
- STRK +52.3 % : DETECTED_EARLY / INTERPRETATION ;
- ARB +25.0 % : DETECTED_EARLY / INTERPRETATION ;
- APT +22.4 % : DETECTED_EARLY / INTERPRETATION ;
- NEAR +21.4 % : DETECTED_EARLY / ENTRY_TIMING_OR_EXECUTION ;
- RAY +21.3 % : DETECTED_EARLY / INTERPRETATION.

Exemples historiques :
- STRK avait ENTRY_WINDOW, opp ~8.4-8.7, mais qualité invalide ;
- APT avait ENTRY_WINDOW, opp ~9.0, mais qualité invalide ;
- RAY avait ENTRY_WINDOW, opp ~8.6, mais INVALID_5M ;
- OP avait ENTRY_WINDOW, opp ~7.9, mais INVALID_5M/15M.

Le moteur a donc souvent vu la structure ; le chemin de décision l'a empêchée de devenir actionnable.

## P2 — Mesures et audit qui peuvent induire en erreur

### P2.1 market_control legacy assimile "absent du top50 publié" à "non détecté"

market_control.py indexe v4_watch.json, lui-même tronqué à OUTPUT_COUNT=50.

Un marché traité par V4 mais hors top50 peut donc apparaître v4_present=false.

Correctif cible : alimenter ce contrôle par toutes les rows V4, pas la vue publique tronquée.

### P2.2 Évaluation historique mélange plusieurs architectures

Snapshot :
- 839 scans ;
- ~360k observations ;
- 515 épisodes d'achat ;
- 182 épisodes complets ;
- EV théorique par trade rempli ~ -3.38 EUR ;
- à 4h/+5% : recall ~30.4 %, précision détection ~19.7 %, précision buy ~8.1 %.

Mais l'historique mélange les versions successives du système et la majorité des outcomes est censurée.

Correctif appliqué / en cours :
- operational_policy explicite ;
- source_commit dans chaque nouveau scan ;
- decision_funnel.json par cycle.

Correctif cible : métriques par cohorte/version, jamais agrégées aveuglément.

## P2 — Alerting / portefeuille

### P2.3 Supervision compte privé non configurée

État actuel : READ_ACCOUNT_OR_ENCRYPTION_SECRET_MISSING.

Conséquence :
- opportunités publiques peuvent être évaluées ;
- mais le système ne connaît pas réellement le cash, les positions, les ordres manuels et le risque déjà engagé ;
- VENDS / PRENDS TES PROFITS / RELÈVE LE STOP ne peut pas fonctionner correctement à partir du compte réel.

### P2.4 Validation finale n'utilise pas encore toute la microstructure disponible

send_useful_alert.py vérifie prix, spread, drift, 15m et plan de risque.
Oracle sait déjà fournir profondeur, slippage et flux de trades publics.

Correctif cible : pour les finalistes uniquement, utiliser Oracle comme validation d'exécution avant alerte.

## Architecture cible

### Plan A — RADAR toujours actif sur Oracle

Oracle devient le radar :
- WebSocket public Bitvavo ticker/trades/candles ;
- tous les marchés EUR actifs ;
- état mémoire permanent ;
- barres canoniques ;
- détection de rank surge, accélération prix/volume, breakout, transition de liquidité ;
- promotion événementielle en quelques secondes ;
- aucune décision de portefeuille à ce stade.

Objectif de conception : p95 de détection candidate < 60-90 s pour un événement émergent.

### Plan B — QUALIFIER adaptatif

Pour les candidats radar :
- 5m/15m/1h/4h frais ;
- trend journalier frais par marché ;
- carnet/profondeur/slippage ;
- opportunity V4 + entry V4 comme baseline ;
- Decision Layer ;
- candidate memory 24-72h ;
- qualité capability-specific, pas un bool global.

### Plan C — DECISION / EXECUTION GATE

Hard veto uniquement pour :
- donnée réellement incertaine / transport manquant ;
- spread / slippage / profondeur incompatibles ;
- structure invalidée ;
- chase excessif ;
- contraintes portefeuille/risk ;
- prix trop éloigné du signal.

Puis :
- validation Oracle fraîche ;
- validation compte read-only ;
- alerte humaine ;
- jamais d'ordre automatique.

### Plan D — AUDIT / REPLAY sur GitHub

GitHub Actions :
- snapshots immuables ;
- replay exact ;
- tests ;
- rapports ;
- évaluation par version ;
- comparaison de politiques.

GitHub ne doit plus servir d'horloge de détection.

## Entonnoir à publier à chaque cycle

decision_funnel.json :
active EUR -> legacy/ingested -> scored -> enriched -> promoted -> valid5m -> valid15m -> data-quality -> watch -> entry-window -> buy-ready -> final-buy.

Chaque perte doit être attribuée à une raison concrète.

## Ce qui empêche d'aller jusqu'au bout immédiatement

1. Pas de canal SSH/terminal connecté à ce chat pour déployer/restart le service Oracle. Le dépôt et les scripts Oracle sont modifiables, et Oracle est interrogeable, mais le serveur lui-même n'est pas administrable depuis les outils actuellement connectés.
2. Credentials Bitvavo read-only + clé de chiffrement de position non configurés dans le workflow.
3. Historique ancien sans version opérationnelle fiable : impossible de prouver rétroactivement la performance du système corrigé comme une cohorte propre.
4. Données historiques fortement censurées et souvent invalidées par l'ancien traitement des gaps.

## Principe directeur

Ne plus demander : "le score est-il bon ?"

Demander dans cet ordre :
1. A-t-on vu le marché assez vite ?
2. Les données utilisées par la décision sont-elles réellement celles que l'on croit ?
3. Le candidat a-t-il été perdu par une règle de plomberie ?
4. La décision structure/timing est-elle cohérente ?
5. L'exécution est-elle encore bonne maintenant ?
6. Le portefeuille peut-il l'absorber ?
7. Après coup, quelle couche a créé chaque faux négatif / faux positif ?

Un changement de score ne doit être envisagé qu'après réponse satisfaisante aux six premières questions.
