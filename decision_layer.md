# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T11:58:31.455693+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HYPE-EUR | action ACHETE_MAINTENANT | opportunité 8.072 | entrée 7.150 | trend 8.750 | rang 7.944
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : SOL-EUR | action LATENT_ACCELERATOR | opportunité 7.570 | entrée 4.500 | trend 8.250 | rang 7.219
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : APT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.576 | entrée 5.950 | trend 8.750 | rang 7.739
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.944
2. FET-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.940
3. DOT-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.877

## Accélération indépendante

- SYRUP-EUR — BUILDING_ACCELERATION — score 5.046/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- WAL-EUR — ACTIVE_NOW — score mémoire 8.533/10 — sources V4 — DETECTED_BUT_TOO_LATE
- ZAMA-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SENT-EUR — ACTIVE_NOW — score mémoire 8.257/10 — sources V4 — WATCH_ONLY
- ZIL-EUR — ACTIVE_NOW — score mémoire 8.197/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 8.087/10 — sources V4 — WATCH_ONLY
- LSK-EUR — MEMORY_24H — score mémoire 8.067/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- IMX-EUR — ACTIVE_NOW — score mémoire 8.040/10 — sources V4 — WATCH_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 7.983/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.971/10 — sources V4 — WATCH_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 7.965/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZAMA-EUR +37.10% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +37.00% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SYN-EUR +33.93% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +32.84% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- STRK-EUR +31.63% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- HEI-EUR +28.90% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- F-EUR +28.12% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- EPIC-EUR +23.82% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +23.19% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CAP-EUR +18.14% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
