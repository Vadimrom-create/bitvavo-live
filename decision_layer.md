# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-26T07:21:56.508480+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : PYTH-EUR | action ACHETE_MAINTENANT | opportunité 8.703 | entrée 6.900 | trend 8.950 | rang 8.220
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : A-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.185 | entrée 6.000 | trend 8.750 | rang 7.857
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : 0G-EUR | action LATENT_ACCELERATOR | opportunité 8.100 | entrée 4.750 | trend 8.950 | rang 7.654
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : GALA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.774 | entrée 7.350 | trend 8.500 | rang 8.143
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. PYTH-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.220
2. EIGEN-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.213
3. DOT-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.207

## Accélération indépendante

- ACT-EUR — CONFIRMED_ACCELERATION — score 8.555/10 — DETECTED_BUT_TOO_LATE
- ZRC-EUR — CONFIRMED_ACCELERATION — score 8.270/10 — DETECTED_BUT_TOO_LATE
- REZ-EUR — CONFIRMED_ACCELERATION — score 7.796/10 — DETECTED_BUT_TOO_LATE
- SOON-EUR — CONFIRMED_ACCELERATION — score 7.390/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ACE-EUR — CONFIRMED_ACCELERATION — score 7.249/10 — DETECTED_BUT_TOO_LATE
- ZRO-EUR — CONFIRMED_ACCELERATION — score 7.055/10 — DETECTED_BUT_TOO_LATE
- BTT-EUR — CONFIRMED_ACCELERATION — score 6.681/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- T-EUR — CONFIRMED_ACCELERATION — score 6.562/10 — DETECTED_BUT_TOO_LATE
- POND-EUR — BUILDING_ACCELERATION — score 6.186/10 — DETECTED_BUT_TOO_LATE
- ALICE-EUR — BUILDING_ACCELERATION — score 6.084/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- FUEL-EUR — MEMORY_24H — score mémoire 9.607/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 9.578/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 8.896/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CTC-EUR — MEMORY_24H — score mémoire 8.874/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ONT-EUR — MEMORY_24H — score mémoire 8.859/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WIN-EUR — MEMORY_24H — score mémoire 8.694/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ACT-EUR — ACTIVE_NOW — score mémoire 8.555/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- 2Z-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZRC-EUR — ACTIVE_NOW — score mémoire 8.270/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- PYTH-EUR — ACTIVE_NOW — score mémoire 8.220/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- POND-EUR +98.86% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +72.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARK-EUR +38.40% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PHA-EUR +38.33% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- 2Z-EUR +31.15% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- AERO-EUR +25.33% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ENA-EUR +21.46% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CC-EUR +18.30% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- KMNO-EUR +17.51% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PUMP-EUR +17.37% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
