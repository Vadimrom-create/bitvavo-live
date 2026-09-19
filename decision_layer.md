# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T12:57:09.646894+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ONDO-EUR | action ACHETE_MAINTENANT | opportunité 9.074 | entrée 7.750 | trend 8.450 | rang 8.044
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : AVAX-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.706 | entrée 6.600 | trend 8.050 | rang 6.744
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : SOL-EUR | action LATENT_ACCELERATOR | opportunité 7.627 | entrée 4.500 | trend 8.250 | rang 7.246
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : JUP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.965 | entrée 6.750 | trend 8.700 | rang 7.771
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ONDO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.044
2. HYPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.898
3. RENDER-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.812

## Accélération indépendante

- CNPY-EUR — BUILDING_ACCELERATION — score 5.639/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- ONDO-EUR — BUILDING_ACCELERATION — score 5.576/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ONDO-EUR — ACTIVE_NOW — score mémoire 8.044/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- RENDER-EUR — ACTIVE_NOW — score mémoire 7.812/10 — sources DECISION_LAYER, V4 — BUYABLE_NOW
- ZAMA-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- GALA-EUR — ACTIVE_NOW — score mémoire 8.153/10 — sources V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 8.093/10 — sources V4 — WATCH_ONLY
- LSK-EUR — MEMORY_24H — score mémoire 8.067/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- KMNO-EUR — ACTIVE_NOW — score mémoire 8.057/10 — sources V4 — WATCH_ONLY
- ZK-EUR — ACTIVE_NOW — score mémoire 8.042/10 — sources V4 — DETECTED_BUT_TOO_LATE
- ZIL-EUR — ACTIVE_NOW — score mémoire 7.989/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- GRT-EUR — ACTIVE_NOW — score mémoire 7.965/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZAMA-EUR +43.54% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- STRK-EUR +40.34% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +37.50% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- EDGE-EUR +35.96% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CAP-EUR +34.69% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +30.58% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- HEI-EUR +29.44% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- F-EUR +25.04% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- XTZ-EUR +24.73% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +21.08% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
