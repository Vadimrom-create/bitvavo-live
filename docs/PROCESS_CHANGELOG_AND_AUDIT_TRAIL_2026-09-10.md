# Traçabilité complète du process et des couches d'amélioration

Date de consolidation : 10 septembre 2026 (Europe/Paris)

Ce document consigne le travail réalisé sur le dépôt `Vadimrom-create/bitvavo-live` jusqu'à cette date afin qu'un tiers — notamment Astra / ChatGPT Work — puisse auditer le process, contester les choix, vérifier les couches successives et distinguer clairement ce qui est historique, figé, expérimental, validé techniquement ou encore non démontré.

## 1. Principe directeur

Le chantier a été volontairement séparé en couches pour éviter de modifier rétroactivement le scanner dès qu'un gagnant récent semblait avoir été raté.

La règle de méthode adoptée est :

1. conserver la V4 comme baseline figée ;
2. rendre ses résultats reproductibles et mesurables ;
3. observer l'ensemble du marché Bitvavo EUR, y compris les marchés exclus de V4 ;
4. mesurer les faux positifs, faux négatifs, données manquantes et exclusions ;
5. séparer strictement détection, décision, gestion du risque, suivi des positions et transport d'alertes ;
6. ne promouvoir une nouvelle politique que sur des résultats prospectifs et hors échantillon ;
7. ne jamais présenter une réussite technique comme une preuve de rentabilité.

La nouvelle `Decision Layer V1` ajoutée le 9 septembre est donc volontairement en **shadow mode**. Elle ne remplace pas V4, ne modifie aucun score V4 et ne peut envoyer aucun ordre réel.

## 2. État initial audité

Référence initiale inspectée : `ab25cdd5951448e6ac889bd1d1b8fd3defc93e12`.

Le fonctionnement initial était, en résumé :

- collecteur public sur marchés EUR avec préfiltre de volume ;
- indicateurs 15m sur un univers filtré ;
- enrichissements 1h/4h et carnets limités par caps ;
- V3 puis V4 avec sélection et enrichissement partiels ;
- stabilisation de certains signaux ;
- email V4 ;
- publication Git / GitHub Pages ;
- présence d'un exécuteur privé préparatoire mais non considéré comme sûr ni activé par ce chantier.

L'audit initial du 8 septembre a établi plusieurs problèmes :

- publication Git pouvant échouer après calcul/email, rendant le feed public ancien ;
- `cancel-in-progress: true` pouvant interrompre un cycle ;
- fraîcheur des données insuffisamment contrôlée ;
- inclusion des bougies en cours dans la baseline V4 ;
- enrichissements partiels et marchés pouvant disparaître silencieusement ;
- non-déterminisme possible lié à l'ordre d'itération Python ;
- contrôle des hausses ne disposant pas d'un historique suffisant pour prouver une détection précoce ;
- journal V4 ne permettant pas de mesurer correctement précision/rappel ;
- absence d'historique complet des décisions négatives ;
- répétitions possibles des emails `REENTRY_READY` ;
- sizing et plafonds de risque insuffisamment robustes ;
- exécuteur privé incomplet et impropre à une activation automatique.

Le détail de cet audit est conservé dans `docs/AUDIT_2026-09-08.md`.

## 3. Couche 1 — gel de V4 et reproductibilité

Objectif : rendre V4 mesurable sans changer sa logique de score.

Principales modifications :

- archive de la baseline V4 de référence ;
- tests d'intégrité empêchant une modification silencieuse des poids, seuils et règles ;
- `PYTHONHASHSEED=0` dans les workflows de validation/replay ;
- enregistrement des entrées nécessaires au replay ;
- replay de V4 sur les mêmes données avec vérification d'égalité stricte ;
- séparation entre comportement historique de V4 et diagnostics nouveaux.

Point important : les bougies en cours restent un comportement hérité de la baseline V4. Les diagnostics ajoutés utilisent des bougies closes, mais ils ne réécrivent pas V4.

Jalon principal : commit `1056ae4d1766047d57c608b11be9e570d479bbf5` — **Preserve V4, measure full universe and supervise held positions**.

## 4. Couche 2 — observation complète de l'univers Bitvavo EUR

Objectif : ne plus confondre « absent du top V4 » et « jamais observé ».

Ajouts :

- collecte de tous les marchés EUR actifs ;
- collecte 5m et 15m sur l'univers complet ;
- validation OHLCV ;
- exclusion des bougies ouvertes pour les diagnostics ;
- détection des trous de cotation ;
- aucune bougie sans transaction n'est inventée ;
- timestamp de récupération distingué du timestamp de marché ;
- contrôles de fraîcheur, dates futures et dernière bougie close ;
- `market_control.json/.txt` pour vérifier les plus fortes hausses du marché contre l'historique de détection.

Cette couche répond directement au problème observé lors des scans manuels : le système pouvait sembler « découvrir » ACU, AERO, FORM, QKC, etc. à partir d'une capture alors que la vraie question était de savoir si V4 les avait effectivement détectées avant le mouvement.

À partir de ce chantier, le principe d'un scan est donc : **lecture prospective V3/V4 + contrôle transversal de l'ensemble des marchés Bitvavo**.

## 5. Couche 3 — journal immuable et évaluation chronologique

Objectif : pouvoir dire a posteriori ce que le système savait réellement à l'instant T.

Ajouts :

- `history/YYYY-MM-DD/<scan_id>.json.gz` append-only ;
- une observation complète par marché et par scan ;
- décisions brutes/stabilisées ;
- features et motifs d'exclusion ;
- premières bougies closes observées conservées sans réécriture silencieuse ;
- index SQLite reconstructible mais non autoritaire ;
- horizons d'évaluation futurs ;
- données incomplètes censurées plutôt que comptées comme échecs ;
- mesure de faux positifs / faux négatifs ;
- distinction observation / épisode d'achat ;
- mesures d'excursion favorable et adverse ;
- critères déclarés avant lecture des résultats.

Le critère principal fixé pour la première évaluation V4 a été : **+5 % dans les quatre heures avec au maximum -5 % d'excursion adverse avant l'objectif**.

Cette couche n'optimise pas V4. Elle permet de savoir où V4 échoue.

Les détails de protocole restent dans `docs/EVALUATION.md` et `docs/DELIVERY_2026-09-08.md`.

## 6. Couche 4 — diagnostics additionnels non intégrés au score V4

Objectif : produire des informations utiles sans polluer la baseline.

Diagnostics ajoutés :

- risque de chase / extension ;
- mèches et structure potentiellement exploitable/dangereuse ;
- récurrence d'un candidat sur plusieurs périodes 15m ;
- proxy structurel « NIL match » ;
- features sur bougies closes : momentum, accélération, volume relatif, ATR, support, distance breakout, extension MA20, consolidation.

Règle : ces diagnostics sont d'abord **descriptifs**. Ils ne prouvent pas une supériorité V5 et ne doivent pas être transformés en probabilités artificielles.

## 7. Couche 5 — gestion du risque et propositions dry-run

Objectif : séparer « bonne opportunité » et « ordre exécutable ».

Ajouts :

- stop fondé sur structure/support et ATR ;
- sizing arrondi vers le bas ;
- prise en compte des minimums d'ordre ;
- plafonds cumulés d'exposition et de perte théorique ;
- contrôle de corrélation entre propositions ;
- objectifs 2R/3R comme scénarios ;
- `proposed_orders.json` toujours en `dry_run=true` ;
- statut de proposition nécessitant validation humaine.

Aucun ordre réel n'est soumis par cette infrastructure.

Les montants de cash/réserve utilisés dans certaines simulations publiques sont des hypothèses de test, pas une lecture du compte privé.

## 8. Couche 6 — publication robuste et alertes utiles

Objectif : empêcher une alerte basée sur un état non publié ou incohérent.

Modifications :

- publication des données avant notification d'achat ;
- push avec fetch/rebase borné ;
- refus d'auto-résoudre un conflit de fichier généré ;
- suppression de `cancel-in-progress: true` ;
- journaux/replay conservés comme artifacts ;
- anti-spam par épisode ;
- cooldown global et par marché ;
- un signal continu identique n'est pas renvoyé indéfiniment ;
- absence d'action = absence d'email ;
- distinction entre échec SMTP et état de décision.

Limite toujours reconnue : SMTP ne fournit pas une vraie clé d'idempotence de bout en bout. Une panne après acceptation par le serveur mais avant persistance locale peut créer une incertitude de livraison.

## 9. Couche 7 — suivi continu des positions détenues

Objectif utilisateur : surveiller les positions réelles à chaque cycle et n'envoyer un email que lorsqu'une action est réellement justifiée.

Commit dédié : `bae1a2eb90ba53fbdcde12a6d379a92dc95f1411` — **Supervise held positions every cycle with encrypted action-only alerts**.

Fonctionnement ajouté :

- lecture Bitvavo privée prévue en **lecture seule** ;
- lecture des soldes et ordres ouverts ;
- supervision de chaque position détenue, même hors top V4 ;
- exécution de cette supervision dans un checkout isolé ;
- possibilité de fonctionner même si la prospection publique échoue ;
- registre privé chiffré/authentifié ;
- statut public sans divulguer les actifs ou soldes privés ;
- aucune route d'exécution/trading privée autorisée par cet adaptateur.

Quatre actions email seulement :

1. `ACHÈTE`
2. `VENDS`
3. `PRENDS PARTIELLEMENT TES PROFITS`
4. `RELÈVE LE STOP`

Règles importantes :

- priorité à la sortie urgente ;
- stop jamais abaissé ;
- prise partielle uniquement si résultat estimé net positif et minimums respectés ;
- relèvement du stop seulement si le nouveau niveau améliore réellement le précédent ;
- absence de justification = silence ;
- état inconnu = jamais interprété comme portefeuille vide.

Correctif de sûreté : commit `216aa6cfbc792662eb110505eff6ffa647fa93fa` — **Keep position exits independent of corrupt prospecting inputs**. Un fichier de prospection corrompu ne doit jamais supprimer une alerte de sortie justifiée.

État au dernier contrôle consigné le 9 septembre à 22:24:50 UTC :

- `status = UNCONFIGURED`
- `mode = READ_ONLY`
- `dry_run = true`
- raison : `READ_ACCOUNT_OR_ENCRYPTION_SECRET_MISSING`
- achats email bloqués car état du compte inconnu.

L'activation réelle nécessite toujours les secrets GitHub documentés dans `docs/POSITION_MONITORING.md`.

## 10. Pourquoi une nouvelle Decision Layer a été ajoutée

Le scanner V4 semblait parfois correctement repérer des profils mais l'interprétation finale était trop binaire : si `Entry` était faible ou si un filtre de timing intervenait, une crypto structurellement forte pouvait disparaître du message final.

Le cas de référence utilisé pour tester cette faiblesse est un profil de type IOST :

- Opportunity ≈ 7,474
- Trend ≈ 7,65
- Entry ≈ 4,5

L'objectif de la couche n'est pas de dire « acheter IOST rétroactivement ». L'objectif est d'empêcher qu'un mauvais score d'entrée instantané efface complètement une structure Opportunity + Trend cohérente.

## 11. Couche 8 — Decision Layer V1 en shadow mode

Commit initial : `d957b817b9073be5ab5fd463ce69c824ae7d1b35` — **Add shadow Decision Layer V1**.

Principe :

- V4 reste figée ;
- `Entry` devient principalement un indicateur de timing ;
- les veto durs doivent être structurels/données/exécution ;
- les candidats sont classés transversalement ;
- la sortie n'est plus seulement « ACHÈTE / rien ».

### 11.1 Quatre buckets obligatoires

- `MEILLEUR_ACHAT_IMMEDIAT`
- `MEILLEURE_LIMITE_PASSIVE`
- `MEILLEUR_LATENT_ACCELERATOR`
- `MEILLEUR_PULLBACK_REENTRY`

Même lorsqu'un bucket est vide, il est explicitement présent dans la sortie.

### 11.2 Seuils actuels, déclarés mais non optimisés

- `LATENT_OPPORTUNITY_MIN = 7.40`
- `LATENT_TREND_MIN = 7.30`
- `IMMEDIATE_ENTRY_MIN = 6.80`
- `PASSIVE_LIMIT_ENTRY_MIN = 5.80`
- `REENTRY_TREND_MIN = 7.60`

Ces seuils sont **heuristiques et pré-déclarés**, pas calibrés sur une performance démontrée.

### 11.3 Classement cross-sectionnel actuel

Le `rank_score` actuel combine :

- 46 % Opportunity ;
- 36 % Trend ;
- 12 % Entry ;
- bonus de récurrence jusqu'à 4 périodes distinctes ;
- pénalité d'extension au-delà de +10 % sur 24 h ;
- pénalité de chase ;
- pénalité de mèche si le champ attendu est présent.

Formule actuelle :

`0.46*Opportunity + 0.36*Trend + 0.12*Entry + 0.06*min(recurrence,4) - 0.035*max(change24-10,0) - 0.055*chase - 0.08*wick`

Ce score est explicitement **un ranking**, pas une probabilité.

### 11.4 Logique de buckets

- achat immédiat : V4 buy-ready + Entry ≥ 6,8 + pas TOO LATE + pas de veto structurel ;
- pullback/re-entry : structure forte et configuration de reprise/pullback avec Trend élevé ;
- limite passive : structure forte avec Entry entre 5,8 et 6,8 ;
- latent accelerator : structure forte mais Entry < 5,8 ;
- sinon WATCH ou veto structurel.

Commit de raffinement : `9df2d08af6e35023051d82596338733628f0fdd0` — **Refine Decision Layer V1 bucket rules**.

Ce commit a notamment :

- corrigé `ILLQUID` → `ILLIQUID` ;
- corrigé la lecture de la récurrence vers `distinct_15m_periods` ;
- séparé limite passive / latent accelerator ;
- exposé les seuils dans le JSON ;
- ajouté `production_orders_enabled = false`.

## 12. Tests de la Decision Layer

Commit : `aeffd34c6c00908cf3e427d040bae28b1cce1784` — **Test Decision Layer V1 including IOST-like case**.

Cas couverts :

- signal type IOST conservé comme `LATENT_ACCELERATOR` malgré Entry faible ;
- défaut structurel de données = vrai veto ;
- buy-ready + bonne entrée = achat immédiat ;
- structure forte + entrée moyenne = limite passive ;
- pullback = re-entry ;
- quatre buckets toujours présents ;
- ordres de production désactivés.

Après intégration de cette couche, la suite de tests complète compte 61 tests et a passé la CI.

## 13. Runner isolé, historique des décisions et intégration au workflow

Commits :

- `38e8d0f9842756c62ed5e8e70df6569d7f30c3b7` — **Add isolated Decision Layer runner and journal**
- `011ee512211aafd93f1020e12b511d3fca805700` — **Integrate shadow Decision Layer into scan workflow**
- `db352541f034da1ccd14f4f2ddc93b1e82fb20ec` — **Publish Decision Layer outputs and journal**

Sorties ajoutées :

- `decision_layer.json`
- `decision_layer.md`
- `decision_history/YYYY-MM-DD/<scan_id>.json.gz`

Le journal de décision est distinct du journal V4. Il permet de comparer plus tard :

- ce que V4 a produit ;
- ce que la Decision Layer a promu/retenu/rejeté ;
- le résultat réel dans 24 h / 72 h ou aux horizons définis.

La Decision Layer n'est pas branchée sur :

- l'envoi d'ordres ;
- l'exécuteur privé ;
- une alerte automatique de production.

Elle est actuellement une couche d'interprétation et de mesure.

## 14. Incident rencontré lors de l'intégration

Le premier run complet de la Decision Layer a échoué uniquement à l'étape shadow avec :

`ModuleNotFoundError: No module named 'research'`

Cause : le script `scripts/run_decision_layer.py` était lancé depuis `scripts/` et le chemin racine du repo n'était pas injecté correctement dans `sys.path`.

Correctif : commit `7d7440c184dce145974563dc762d909d60ef6fb9` — **Fix Decision Layer runner import path**.

Après ce correctif :

- tests critiques : succès ;
- collecte/scanner : succès ;
- replay V4 : succès ;
- Decision Layer : succès ;
- publication : succès ;
- supervision positions : étape exécutée ;
- Pages : succès.

Le dernier cycle complet vérifié s'est terminé avec succès le 9 septembre à 22:25 UTC environ.

## 15. Dernier résultat réel de la Decision Layer au moment de cette consolidation

Sur le scan publié à 22:23:41 UTC le 9 septembre :

- aucun `MEILLEUR_ACHAT_IMMEDIAT` ;
- aucune `MEILLEURE_LIMITE_PASSIVE` ;
- aucun `MEILLEUR_LATENT_ACCELERATOR` ;
- meilleur `MEILLEUR_PULLBACK_REENTRY` : `USELESS-EUR` ;
- autres candidats top re-entry : `SYRUP-EUR`, `VVV-EUR`.

Ce résultat n'est pas une recommandation intemporelle : il sert ici uniquement de preuve que la couche a effectivement tourné sur un scan réel.

## 16. Ce qui est figé / ce qui est expérimental / ce qui est inactif

### Figé / baseline

- règles et seuils V4 ;
- replay de compatibilité ;
- archive de référence ;
- instrumentation destinée à mesurer V4.

### Infrastructure considérée comme active

- collecte publique ;
- contrôle de fraîcheur ;
- journal `history/` ;
- évaluation ;
- market control ;
- publication robuste ;
- CI ;
- génération des sorties Decision Layer en shadow.

### Expérimental / à auditer

- seuils Decision Layer ;
- pondérations du `rank_score` ;
- statut exact des veto structurels ;
- définition de `pullback_like` ;
- pénalités chase / wick ;
- horizon pertinent pour juger les buckets ;
- éventuelle future calibration des probabilités.

### Prévu mais non actif sur compte réel au dernier contrôle

- monitoring privé Bitvavo : `UNCONFIGURED` faute de secrets/paramètres ;
- alertes d'achat fondées sur état réel du compte ;
- exécution réelle : volontairement désactivée.

## 17. Faiblesses et points de contrôle externe à ne pas masquer

### 17.1 Decision Layer encore heuristique

Les seuils 7,40 / 7,30 / 6,80 / 5,80 / 7,60 et les poids 46/36/12 ne proviennent pas encore d'une optimisation prospective validée. Ils ont été choisis pour rendre testable une hypothèse de décision : « Entry ne doit pas effacer une structure forte ».

Astra/Work doit challenger ces valeurs et surtout vérifier qu'une éventuelle optimisation future utilise un échantillon de développement séparé d'un échantillon de validation.

### 17.2 Risque de sur-veto par qualité de données

La couche traite notamment `INVALID_5M`, `INVALID_15M`, `MISSING_5M`, `MISSING_15M`, `LOW_LIQUIDITY` et `WIDE_SPREAD_RISK` comme veto structurels.

Or, sur plusieurs scans, une faible fraction seulement des 400+ marchés dispose simultanément de fenêtres 5m/15m jugées pleinement valides. Cela protège contre de mauvaises données mais peut créer un rappel très faible et reproduire, sous une autre forme, le problème initial de faux négatifs.

Question d'audit : distinguer les défauts qui rendent **l'opportunité impossible à évaluer** de ceux qui rendent seulement **l'exécution immédiate impossible**.

### 17.3 Vérification de l'intégration des diagnostics de mèches

Le classement lit actuellement `(obs['wick_setup'] or {}).get('is_wick_setup')`, alors que le producteur historique de diagnostic de mèches expose principalement un champ `status` (`NORMAL`, `POTENTIALLY_EXPLOITABLE`, `WAIT_FOR_DIRECTION`, `DANGEROUS_STRUCTURE`).

Cela doit être vérifié de bout en bout. Si aucun `is_wick_setup` n'est injecté ailleurs, la pénalité de mèche du `rank_score` peut être inactive en pratique.

**Ce point est volontairement consigné comme hypothèse de bug/intégration à vérifier, pas comme bug définitivement prouvé.**

### 17.4 Pullback/re-entry simplifié

`pullback_like` est actuellement vrai si :

- état `ENTRY_WINDOW` ou `REENTRY_READY`, ou
- flag `WICK_SETUP`, ou
- variation 24 h négative.

Cette définition est simple et peut être trop large. Une variation 24 h négative n'est pas forcément un pullback dans une tendance haussière exploitable.

### 17.5 Le ranking n'est pas une probabilité

Aucune probabilité +10/+20/+30/+40 % ne doit être déduite du `rank_score`. Toute calibration de probabilités doit être une couche séparée avec reliability curves / Brier score / calibration hors échantillon si l'échantillon devient suffisant.

### 17.6 Données et cadence

GitHub Actions ne garantit pas une exécution toutes les 5 minutes. Les cycles observés ont souvent été plus lents. La stratégie doit être évaluée sur la cadence réelle, pas sur le cron théorique.

### 17.7 Historique encore jeune

Les premières statistiques V4 comportent beaucoup de données censurées et peu d'épisodes d'achat mûrs. Il est trop tôt pour conclure à une EV ou à une supériorité de la nouvelle couche.

### 17.8 Monitoring privé non encore validé en conditions réelles

Les tests du monitoring sont solides techniquement, mais au dernier statut public la lecture du compte n'est pas configurée. Une validation réelle en lecture seule reste nécessaire avant de considérer cette couche opérationnelle.

## 18. Ce qu'un reviewer doit comparer

Le reviewer ne doit pas simplement relire le code actuel. Il doit comparer les couches successives :

1. V4 historique seule ;
2. V4 + instrumentation / qualité / journal ;
3. V4 + market control ;
4. V4 + suivi chronologique des faux négatifs ;
5. V4 + Decision Layer V1 shadow ;
6. éventuellement future Decision Layer V2, mais seulement après définition pré-enregistrée.

Pour chaque couche :

- améliore-t-elle réellement le rappel des mouvements utiles ?
- augmente-t-elle excessivement les faux positifs ?
- ajoute-t-elle une information nouvelle ou double-t-elle un signal existant ?
- introduit-elle une fuite temporelle ?
- réagit-elle à une donnée disponible réellement au moment du signal ?
- ses seuils ont-ils été choisis avant ou après observation des résultats ?
- son résultat serait-il identique sur replay ?

## 19. Commits méthodologiques principaux

Les nombreux commits automatiques `Record fresh scan...` et `Persist alert delivery state` sont des publications de données/état, pas des changements méthodologiques.

Commits de méthode principaux à auditer :

- `1056ae4d1766047d57c608b11be9e570d479bbf5` — gel V4 + mesure univers complet + monitoring intégré ;
- `bae1a2eb90ba53fbdcde12a6d379a92dc95f1411` — suivi des positions à chaque cycle ;
- `216aa6cfbc792662eb110505eff6ffa647fa93fa` — sorties indépendantes d'une prospection corrompue ;
- `d957b817b9073be5ab5fd463ce69c824ae7d1b35` — Decision Layer V1 shadow ;
- `9df2d08af6e35023051d82596338733628f0fdd0` — raffinement des buckets / récurrence / seuils exposés ;
- `aeffd34c6c00908cf3e427d040bae28b1cce1784` — tests Decision Layer incluant IOST-like ;
- `38e8d0f9842756c62ed5e8e70df6569d7f30c3b7` — runner isolé et journal de décision ;
- `011ee512211aafd93f1020e12b511d3fca805700` — intégration workflow ;
- `db352541f034da1ccd14f4f2ddc93b1e82fb20ec` — publication des sorties/journal ;
- `7d7440c184dce145974563dc762d909d60ef6fb9` — correction du chemin d'import du runner.

## 20. Critère de réussite du chantier

Le chantier ne sera pas considéré comme réussi parce que :

- les tests passent ;
- GitHub Actions est vert ;
- une crypto citée ensuite monte ;
- la Decision Layer produit davantage de candidats.

Le critère réel est : **meilleure qualité de décision prospective**, mesurée sur une période suffisamment longue, avec amélioration du rappel utile sans explosion des faux positifs ni du risque, et comparaison contre V4 figée sur les mêmes fenêtres.

Toute couche qui n'améliore pas ce compromis doit être supprimée ou révisée, même si sa logique paraît séduisante.
