# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T07:14:33.280687+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : AVAX-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.090 | entrée 7.850 | trend 7.600 | rang 7.431
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. AVAX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.431
2. STX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.371
3. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.360

## Accélération indépendante

- C-EUR — BUILDING_ACCELERATION — score 5.909/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- KAS-EUR — ACTIVE_NOW — score mémoire 8.406/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 8.014/10 — sources V4 — WATCH_ONLY
- ZAMA-EUR — MEMORY_24H — score mémoire 7.960/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- NPC-EUR — MEMORY_24H — score mémoire 7.903/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 7.873/10 — sources V4 — WATCH_ONLY
- RED-EUR — ACTIVE_NOW — score mémoire 7.846/10 — sources V4 — WATCH_ONLY
- DOT-EUR — MEMORY_24H — score mémoire 7.831/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- ETC-EUR — MEMORY_24H — score mémoire 7.770/10 — sources V4 — MEMORY_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.753/10 — sources V4 — WATCH_ONLY
- ZIG-EUR — ACTIVE_NOW — score mémoire 7.706/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CELR-EUR +91.20% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +50.27% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- C-EUR +43.55% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZAMA-EUR +37.89% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIL-EUR +23.50% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SKL-EUR +21.19% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CTSI-EUR +17.80% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- AVAX-EUR +14.66% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ONG-EUR +14.47% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- AVA-EUR +14.12% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
