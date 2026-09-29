# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-29T13:58:30.130358+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : GALA-EUR | action ACHETE_MAINTENANT | opportunité 9.119 | entrée 7.150 | trend 9.000 | rang 8.434
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : VIRTUAL-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.721 | entrée 6.700 | trend 8.350 | rang 7.602
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : MIOTA-EUR | action LATENT_ACCELERATOR | opportunité 7.795 | entrée 4.950 | trend 8.900 | rang 7.623
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : XLM-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.287 | entrée 8.150 | trend 9.000 | rang 8.234
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. GALA-EUR — ACHETE_MAINTENANT — rank 8.434 — opportunité 9.119 — entrée 7.150 — trend 9.000
2. CFG-EUR — ACHETE_MAINTENANT — rank 7.980 — opportunité 8.751 — entrée 7.000 — trend 8.150
3. NEAR-EUR — ACHETE_MAINTENANT — rank 7.816 — opportunité 8.969 — entrée 7.900 — trend 7.300
4. ENA-EUR — ACHETE_MAINTENANT — rank 7.491 — opportunité 8.127 — entrée 6.900 — trend 7.900
5. SHIB-EUR — ACHETE_MAINTENANT — rank 6.820 — opportunité 8.227 — entrée 7.400 — trend 5.450

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. GALA-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.434
2. XLM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.234
3. LINK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.115

## Accélération indépendante

- USELESS-EUR — CONFIRMED_ACCELERATION — score 9.062/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ROSE-EUR — CONFIRMED_ACCELERATION — score 9.045/10 — DETECTED_BUT_TOO_LATE
- NEAR-EUR — CONFIRMED_ACCELERATION — score 8.976/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- INIT-EUR — CONFIRMED_ACCELERATION — score 8.113/10 — DETECTED_BUT_TOO_LATE
- XAN-EUR — BUILDING_ACCELERATION — score 6.275/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ICX-EUR — BUILDING_ACCELERATION — score 6.106/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SOON-EUR — BUILDING_ACCELERATION — score 5.628/10 — DETECTED_BUT_TOO_LATE
- CSPR-EUR — BUILDING_ACCELERATION — score 5.448/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- STRK-EUR — BUILDING_ACCELERATION — score 4.931/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- NEAR-EUR — ACTIVE_NOW — score mémoire 8.976/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ENA-EUR — ACTIVE_NOW — score mémoire 7.491/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- GIGA-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- QUID-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- USELESS-EUR — ACTIVE_NOW — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ROSE-EUR — ACTIVE_NOW — score mémoire 9.045/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- SWELL-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DGB-EUR — MEMORY_24H — score mémoire 8.836/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DYDX-EUR — MEMORY_24H — score mémoire 8.690/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- 0G-EUR +39.03% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CELO-EUR +23.32% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CRV-EUR +21.70% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- POND-EUR +21.28% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZBCN-EUR +20.88% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- CVX-EUR +18.12% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- SYRUP-EUR +17.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AAVE-EUR +16.23% — DETECTED_EARLY — couche NONE — action NONE
- GRASS-EUR +16.17% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ICP-EUR +15.82% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Gestion des positions détenues

Policy : STAGED_10_20_RUNNER_V1
- +10% : prise partielle 35%.
- +20% : seconde prise 35%.
- Runner conservé : 30%.
- Revue coût d'opportunité après 72 h ; sortie seulement avant la première partielle, proche/sous le PRU et avec momentum 15m affaibli.
- Pas de stop serré mécaniquement après une petite hausse ; le stop reste lié à l'invalidation structurelle.

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
