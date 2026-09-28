# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-28T12:26:52.547421+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : KAS-EUR | action ACHETE_MAINTENANT | opportunité 8.185 | entrée 6.850 | trend 8.700 | rang 7.782
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : XDC-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.113 | entrée 5.800 | trend 9.000 | rang 7.852
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : GRAM-EUR | action LATENT_ACCELERATOR | opportunité 7.559 | entrée 4.500 | trend 8.750 | rang 7.365
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : WLD-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.229 | entrée 7.150 | trend 8.650 | rang 7.882
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. KAS-EUR — ACHETE_MAINTENANT — rank 7.782 — opportunité 8.185 — entrée 6.850 — trend 8.700
2. BCH-EUR — ACHETE_MAINTENANT — rank 7.685 — opportunité 8.563 — entrée 7.400 — trend 7.550
3. SEI-EUR — ACHETE_MAINTENANT — rank 7.628 — opportunité 8.372 — entrée 7.750 — trend 8.600
4. ADA-EUR — ACHETE_MAINTENANT — rank 7.290 — opportunité 8.902 — entrée 7.350 — trend 6.750
5. POL-EUR — ACHETE_MAINTENANT — rank 6.543 — opportunité 8.341 — entrée 6.900 — trend 5.400

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. WLD-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.882
2. XDC-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.852
3. PYTH-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.829

## Accélération indépendante

- ARX-EUR — CONFIRMED_ACCELERATION — score 9.471/10 — DETECTED_BUT_TOO_LATE
- XLM-EUR — CONFIRMED_ACCELERATION — score 9.165/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LINK-EUR — CONFIRMED_ACCELERATION — score 8.801/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- POL-EUR — CONFIRMED_ACCELERATION — score 8.711/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GRASS-EUR — CONFIRMED_ACCELERATION — score 8.398/10 — DETECTED_BUT_TOO_LATE
- HBAR-EUR — CONFIRMED_ACCELERATION — score 8.323/10 — DETECTED_BUT_TOO_LATE
- CRO-EUR — CONFIRMED_ACCELERATION — score 8.137/10 — DETECTED_BUT_TOO_LATE
- GRT-EUR — CONFIRMED_ACCELERATION — score 7.792/10 — DETECTED_BUT_TOO_LATE
- VELO-EUR — CONFIRMED_ACCELERATION — score 7.734/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- VIRTUAL-EUR — CONFIRMED_ACCELERATION — score 7.532/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- POL-EUR — ACTIVE_NOW — score mémoire 8.711/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ADA-EUR — ACTIVE_NOW — score mémoire 7.290/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- WMTX-EUR — MEMORY_24H — score mémoire 9.914/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NMR-EUR — MEMORY_24H — score mémoire 9.777/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ARX-EUR — ACTIVE_NOW — score mémoire 9.471/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- BTT-EUR — MEMORY_24H — score mémoire 9.434/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XLM-EUR — ACTIVE_NOW — score mémoire 9.165/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LINK-EUR — ACTIVE_NOW — score mémoire 8.801/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.779/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FUEL-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- QNT-EUR +44.86% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- HBAR-EUR +30.08% — DETECTED_EARLY — couche NONE — action NONE
- GRT-EUR +16.83% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NMR-EUR +14.89% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PUMP-EUR +13.29% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ALGO-EUR +12.46% — DETECTED_EARLY — couche NONE — action NONE
- MON-EUR +10.63% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MIOTA-EUR +9.55% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- IKA-EUR +8.98% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- SEI-EUR +8.96% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
