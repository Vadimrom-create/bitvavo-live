# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T01:44:54.431613+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : HYPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.794 | entrée 7.450 | trend 8.250 | rang 7.631
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.631
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.771
3. STRK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 4.701

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- SYN-EUR — MEMORY_24H — score mémoire 8.311/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- VTHO-EUR — MEMORY_24H — score mémoire 8.268/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PEPE-EUR — MEMORY_24H — score mémoire 8.255/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AVAX-EUR — ACTIVE_NOW — score mémoire 8.026/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- PROVE-EUR — ACTIVE_NOW — score mémoire 7.973/10 — sources V4 — WATCH_ONLY
- YB-EUR — MEMORY_24H — score mémoire 7.953/10 — sources V4 — MEMORY_ONLY
- VVV-EUR — ACTIVE_NOW — score mémoire 7.862/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 7.827/10 — sources ACCELERATION, V4 — WATCH_ONLY
- COW-EUR — MEMORY_24H — score mémoire 7.799/10 — sources V4 — MEMORY_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.749/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- G-EUR +43.47% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +41.96% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- F-EUR +38.63% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZAMA-EUR +24.61% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- APT-EUR +21.66% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +20.77% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- S-EUR +20.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIG-EUR +20.63% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QKC-EUR +20.55% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SKY-EUR +19.91% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
