# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T05:27:44.479186+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : HYPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.635 | entrée 6.700 | trend 7.950 | rang 7.374
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.374
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.112
3. SOL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.525

## Accélération indépendante

- G-EUR — CONFIRMED_ACCELERATION — score 6.843/10 — DETECTED_BUT_TOO_LATE
- STRK-EUR — BUILDING_ACCELERATION — score 5.276/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- C-EUR — MEMORY_24H — score mémoire 8.647/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- S-EUR — ACTIVE_NOW — score mémoire 8.250/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ZAMA-EUR — MEMORY_24H — score mémoire 7.949/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NPC-EUR — MEMORY_24H — score mémoire 7.903/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DOT-EUR — MEMORY_24H — score mémoire 7.831/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- VVV-EUR — ACTIVE_NOW — score mémoire 7.828/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.811/10 — sources V4 — WATCH_ONLY
- COW-EUR — ACTIVE_NOW — score mémoire 7.799/10 — sources V4 — WATCH_ONLY
- ETC-EUR — MEMORY_24H — score mémoire 7.770/10 — sources V4 — MEMORY_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.722/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CELR-EUR +105.60% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +64.51% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZAMA-EUR +35.60% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CTSI-EUR +33.96% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZIL-EUR +28.04% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- C-EUR +23.80% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SKL-EUR +19.14% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- HEI-EUR +14.45% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- STX-EUR +13.40% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- STRK-EUR +13.34% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
