# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T23:56:20.690946+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LINK-EUR | action ACHETE_MAINTENANT | opportunité 8.382 | entrée 7.550 | trend 9.000 | rang 8.196
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : AXS-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.251 | entrée 6.100 | trend 9.000 | rang 7.884
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : SIGN-EUR | action LATENT_ACCELERATOR | opportunité 7.877 | entrée 4.500 | trend 8.950 | rang 7.613
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ZK-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.729 | entrée 6.300 | trend 8.950 | rang 8.127
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. LINK-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.196
2. WAL-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.146
3. ZK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.127

## Accélération indépendante

- POND-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- SSV-EUR — CONFIRMED_ACCELERATION — score 8.917/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CELO-EUR — BUILDING_ACCELERATION — score 6.096/10 — DETECTED_BUT_TOO_LATE
- WIF-EUR — BUILDING_ACCELERATION — score 5.474/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRUST-EUR — BUILDING_ACCELERATION — score 5.075/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SAFE-EUR — BUILDING_ACCELERATION — score 4.891/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- XPL-EUR — ACTIVE_NOW — score mémoire 7.997/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- WIF-EUR — ACTIVE_NOW — score mémoire 7.683/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- POND-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- PONKE-EUR — MEMORY_24H — score mémoire 9.578/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 8.975/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SSV-EUR — ACTIVE_NOW — score mémoire 8.917/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CTC-EUR — MEMORY_24H — score mémoire 8.874/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- NIL-EUR — MEMORY_24H — score mémoire 8.667/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ARK-EUR — MEMORY_24H — score mémoire 8.526/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- LINK-EUR — ACTIVE_NOW — score mémoire 8.196/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- PHA-EUR +67.35% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- POND-EUR +65.05% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARK-EUR +30.85% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +24.03% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AERO-EUR +21.57% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SEI-EUR +19.20% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ENA-EUR +18.85% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- WMTX-EUR +18.65% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRASS-EUR +18.18% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +18.05% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
