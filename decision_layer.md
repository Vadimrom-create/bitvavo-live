# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-13T23:45:56.063321+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : VTHO-EUR | action LATENT_ACCELERATOR | opportunité 7.959 | entrée 4.950 | trend 9.200 | rang 7.061
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : WLD-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.566 | entrée 6.050 | trend 8.150 | rang 7.380
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. WLD-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.380
2. VTHO-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.061

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- YB-EUR — ACTIVE_NOW — score mémoire 8.001/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.977/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.716/10 — sources V4 — WATCH_ONLY
- APT-EUR — MEMORY_24H — score mémoire 7.715/10 — sources V4 — MEMORY_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.712/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.666/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.607/10 — sources V4 — WATCH_ONLY
- ZIG-EUR — MEMORY_24H — score mémoire 7.576/10 — sources V4 — MEMORY_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.521/10 — sources V4 — WATCH_ONLY
- TREE-EUR — MEMORY_24H — score mémoire 7.466/10 — sources V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- LSK-EUR +145.58% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- CVC-EUR +35.18% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZKJ-EUR +23.32% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- IQ-EUR +18.12% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- FIL-EUR +18.09% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VTHO-EUR +15.90% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOLV-EUR +12.58% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- BIRB-EUR +11.41% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- POWR-EUR +10.21% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIL-EUR +8.92% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
