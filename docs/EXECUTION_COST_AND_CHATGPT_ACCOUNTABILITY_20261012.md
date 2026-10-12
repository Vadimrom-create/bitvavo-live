# Solaire — coût des rejets et des décisions ChatGPT (12 octobre 2026)

**Périmètre : mesure uniquement.** Aucun changement de seuil de production, d'envoi d'email, de gate BUY ou d'envoi d'ordre. Suivi central : [#134](https://github.com/Vadimrom-create/bitvavo-live/issues/134).

## Constats vérifiés avant cette proposition

- `scripts/send_production_buy_alert.py` rejette sous `MIN_QUOTE_VOLUME_EUR = 75_000` **avant** de demander le carnet. Le cas [GTC du 12 octobre à 07:16 UTC](../execution_observations/observation_1cc45afe08b6232c396dd8ccb8753b00.json) est `INSUFFICIENT_EXECUTION_LIQUIDITY` avec `raw_book=null` et `BOOK_NOT_REQUESTED_OR_UNAVAILABLE`. On ne peut pas reconstituer une exécution au moment du rejet à partir d'un carnet actuel.
- `scripts/update_emerging_liquidity_shadow.py` surveille déjà une partie des signaux à volume faible en mesure prospective. Le statut archivé le **12 octobre à 16:14 UTC** comporte 4 signaux : 3 `STRUCTURAL_RANGE_TOO_NARROW`, 1 `SPREAD_TOO_WIDE`, et 0 cas `ONLY_24H_VOLUME_GATE_BLOCKS`. Il ne démontre pas que le filtre des 75k € était sans coût sur d'autres cycles.
- Le statut production du **12 octobre à 17:55 UTC** indique un nouveau rejet OGN `STRUCTURAL_STOP_TOO_WIDE`. Chaque épisode doit être jugé à sa propre heure : une alerte plus ancienne ne valide pas automatiquement une nouvelle entrée.
- `docs/SCAN_DECISION_ACCOUNTABILITY_V1.md` et `scripts/scan_accountability_ledger.py` existent, mais les décisions ChatGPT et les fills réels ne sont pas capturés automatiquement. La valeur nette marginale de ChatGPT reste **NON_MESURABLE**, sans journal privé et paires exécutables vérifiées.

## Amélioration limitée au shadow de liquidité

1. Conserver les mises historiques **100 et 250 €** et ajouter **125 et 150 €**, sans changer les critères de détection ni les seuils d'acceptation shadow (`BOOK_IMPACT_REFERENCE_PCT`, `TURNOVER_MULTIPLE_MIN`).
2. Conserver `roundtrip_cost_pct` (achat au carnet puis liquidation instantanée au **même** carnet, avant frais) et ajouter `roundtrip_after_fees_pct_est` avec frais hypothétiques de **0,25 % de chaque côté**.
3. Ajouter `roundtrip_stressed_pct_est` avec un supplément défavorable supposé de **0,10 % de chaque côté**, en plus des frais de 0,25 %. Ces hypothèses ne représentent **pas** le tarif vérifié de l'utilisateur ni une cotation d'exécution future.
4. Retourner `null` pour ces coûts si la profondeur observée ne couvre pas l'entrée et la sortie. Un indicateur `direct_exec_pass` favorable ne prouve ni un remplissage réel, ni la capacité future à vendre.
5. Ne **pas** recalculer les événements passés comme si les carnets courants avaient été connus au moment du signal. Nouvelles colonnes disponibles seulement à partir des nouvelles collectes après activation de ce code.

## Protocole d'attribution à appliquer aux neuf gagnants du 12 octobre

Cohorte d'enquête : `GTC, RSR, OSMO, CTK, RDNT, W, OGN, PYTH, CT`. Les hausses de la capture sont des **classements a posteriori**, pas des rendements d'investissement.

Pour chaque **épisode indépendant**, joindre dans l'ordre chronologique : première détection, première alerte envoyée, premier rejet (avec raison), premier carnet horodaté, révalidations, décisions ChatGPT effectivement formulées, plan d'entrée/stop/sortie et issues jusqu'à l'horizon maturé. Source absente = `INCONNU`, jamais `NON_DETECTE` par défaut.

Classes mutuellement exclusives par décision : `NON_OBSERVÉ`, `DÉTECTÉ_SANS_ALERTE`, `REJETÉ_NON_EXÉCUTABLE`, `REJETÉ_EXÉCUTABLE_SHADOW`, `ALERTE_ACHÈTE_SANS_RECOMMANDATION`, `ACHÈTE_REFUSÉ_CHATGPT`, `RECOMMANDÉ_NON_EXÉCUTÉ`, `EXÉCUTÉ`, `DONNÉES_INSUFFISANTES`. Un même marché peut traverser plusieurs états au cours du temps.

### Preuve économique minimale

- **Faisabilité de l'entrée** : carnet *au moment de la décision*, ask/VWAP, largeur de spread, frais, profondeur, limite réalisable, volatilité/stop. Pas de fill passif supposé gratuit.
- **Maturation** : suivre 4/24/48/72 h/7 jours ; 1/4 h existe dans le shadow de liquidité, les autres horizons et les prix de sortie exécutables restent à instrumenter séparément.
- **Trajectoire** : comparer stop avant TP en cas de bougie ambiguë, position/risque engagés et expositions concurrentes, coût de sortie non connu = `NON_MESURABLE` ; MFE, MAE ou cours de capture ne sont pas un PnL.
- **Comparaison appariée** : Solaire seul, Solaire + ChatGPT et HUMAN SWING R2 sur mêmes signaux, mise, horaires et règles de sortie ; exposer N signaux, N fills, N maturés, PnL net, drawdown et temps humain.
- **Antibiais** : inclure les signaux faibles et les pertes, non seulement les gagnants choisis a posteriori ; ne pas ajuster les seuils sur cette cohorte.

### Critère de progression

Avant toute modification du filtre de volume en production : observer prospectivement un nombre suffisant d'épisodes indépendants passés au carnet à 125/150 €, avec leurs issues mûres et frais vérifiables, puis montrer **un bénéfice net robuste face à la politique actuelle**, incluant les pertes supplémentaires. Une observation de faisabilité isolée ne suffit pas.

**Statut au 12/10/2026 :** instrumentation des tailles et coûts en PR, rentabilité additionnelle du filtre par carnet **non démontrée**, contribution de ChatGPT **non mesurable** sans appariement privé.
