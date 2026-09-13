# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-13T22:57:53.199054+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : VTHO-EUR | action LATENT_ACCELERATOR | opportunité 7.798 | entrée 5.250 | trend 9.200 | rang 6.785
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : VET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.947 | entrée 7.200 | trend 8.650 | rang 7.874
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.874
2. VTHO-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 6.785

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- LDO-EUR — ACTIVE_NOW — score mémoire 7.985/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.874/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.733/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.726/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.718/10 — sources V4 — WATCH_ONLY
- APT-EUR — MEMORY_24H — score mémoire 7.715/10 — sources V4 — MEMORY_ONLY
- ZIG-EUR — MEMORY_24H — score mémoire 7.576/10 — sources V4 — MEMORY_ONLY
- TREE-EUR — MEMORY_24H — score mémoire 7.466/10 — sources V4 — MEMORY_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 7.428/10 — sources V4 — WATCH_ONLY
- LINK-EUR — MEMORY_24H — score mémoire 7.422/10 — sources V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- LSK-EUR +226.52% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- CVC-EUR +50.58% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- VTHO-EUR +19.70% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZKJ-EUR +17.76% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FIL-EUR +16.44% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- IQ-EUR +14.22% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- REZ-EUR +14.11% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SOLV-EUR +12.40% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- POWR-EUR +10.10% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIL-EUR +9.30% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
