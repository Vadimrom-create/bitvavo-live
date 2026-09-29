# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-29T05:52:38.183702+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : KAS-EUR | action ACHETE_MAINTENANT | opportunité 8.957 | entrée 7.450 | trend 7.550 | rang 7.836
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : CELO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.157 | entrée 6.000 | trend 8.500 | rang 7.168
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ORCA-EUR | action LATENT_ACCELERATOR | opportunité 8.318 | entrée 4.950 | trend 7.500 | rang 7.180
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : LINK-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.253 | entrée 7.250 | trend 8.900 | rang 8.034
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. KAS-EUR — ACHETE_MAINTENANT — rank 7.836 — opportunité 8.957 — entrée 7.450 — trend 7.550
2. AVAX-EUR — ACHETE_MAINTENANT — rank 6.921 — opportunité 8.661 — entrée 7.850 — trend 5.700
3. ADA-EUR — ACHETE_MAINTENANT — rank 6.817 — opportunité 8.275 — entrée 7.850 — trend 5.700
4. BNB-EUR — ACHETE_MAINTENANT — rank 6.286 — opportunité 8.102 — entrée 6.950 — trend 4.650

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. LINK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.034
2. KAS-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.836
3. SEI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.791

## Accélération indépendante

- CSPR-EUR — CONFIRMED_ACCELERATION — score 9.687/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- STRK-EUR — CONFIRMED_ACCELERATION — score 6.667/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MEME-EUR — BUILDING_ACCELERATION — score 6.361/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- 0G-EUR — BUILDING_ACCELERATION — score 6.126/10 — DETECTED_BUT_TOO_LATE
- POND-EUR — BUILDING_ACCELERATION — score 6.000/10 — DETECTED_BUT_TOO_LATE
- NOM-EUR — BUILDING_ACCELERATION — score 5.983/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRAC-EUR — BUILDING_ACCELERATION — score 5.262/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XDP-EUR — BUILDING_ACCELERATION — score 5.207/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GNO-EUR — BUILDING_ACCELERATION — score 5.004/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HAEDAL-EUR — BUILDING_ACCELERATION — score 4.821/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ICP-EUR — ACTIVE_NOW — score mémoire 7.197/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- CSPR-EUR — ACTIVE_NOW — score mémoire 9.687/10 — sources ACCELERATION, V4 — WATCH_ONLY
- PUFFER-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 8.844/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- IMU-EUR — MEMORY_24H — score mémoire 8.632/10 — sources ACCELERATION — MEMORY_ONLY
- QUID-EUR — MEMORY_24H — score mémoire 8.100/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- LINK-EUR — ACTIVE_NOW — score mémoire 8.034/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- OSMO-EUR — MEMORY_24H — score mémoire 7.990/10 — sources ACCELERATION — MEMORY_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.836/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- NMR-EUR +36.87% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HBAR-EUR +23.32% — DETECTED_EARLY — couche NONE — action NONE
- CRV-EUR +19.04% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- 0G-EUR +17.77% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ALGO-EUR +16.04% — DETECTED_EARLY — couche NONE — action NONE
- POND-EUR +14.95% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CELO-EUR +11.04% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARX-EUR +9.73% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MIOTA-EUR +8.99% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CVX-EUR +8.46% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
