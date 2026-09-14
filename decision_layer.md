# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-13T23:59:01.188277+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : VTHO-EUR | action LATENT_ACCELERATOR | opportunité 7.644 | entrée 5.200 | trend 9.200 | rang 6.867
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : WLD-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.151 | entrée 6.050 | trend 8.150 | rang 7.189
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Top cross-sectionnel

1. WLD-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.189
2. VTHO-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 6.867

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- LDO-EUR — ACTIVE_NOW — score mémoire 7.914/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.903/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.721/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- APT-EUR — MEMORY_24H — score mémoire 7.715/10 — sources V4 — MEMORY_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.673/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.590/10 — sources V4 — WATCH_ONLY
- ZIG-EUR — MEMORY_24H — score mémoire 7.576/10 — sources V4 — MEMORY_ONLY
- TREE-EUR — MEMORY_24H — score mémoire 7.466/10 — sources V4 — MEMORY_ONLY
- PORTAL-EUR — ACTIVE_NOW — score mémoire 7.440/10 — sources V4 — WATCH_ONLY
- LINK-EUR — MEMORY_24H — score mémoire 7.422/10 — sources V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- LSK-EUR +154.55% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CVC-EUR +36.08% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZKJ-EUR +22.25% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- IQ-EUR +20.02% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- FIL-EUR +18.17% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VTHO-EUR +17.16% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOLV-EUR +14.11% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- POWR-EUR +11.92% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- BIRB-EUR +9.74% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- ZIL-EUR +8.95% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
