# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T02:34:37.130518+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ADA-EUR | action ACHETE_MAINTENANT | opportunité 8.593 | entrée 8.200 | trend 6.200 | rang 7.141
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : HYPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.984 | entrée 7.600 | trend 8.250 | rang 7.711
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.711
2. ONDO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.526
3. ENA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.323

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- SYN-EUR — MEMORY_24H — score mémoire 8.620/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- BEAM-EUR — ACTIVE_NOW — score mémoire 8.269/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — MEMORY_24H — score mémoire 8.268/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PEPE-EUR — MEMORY_24H — score mémoire 8.255/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.047/10 — sources ACCELERATION, V4 — WATCH_ONLY
- NPC-EUR — ACTIVE_NOW — score mémoire 8.035/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 7.917/10 — sources V4 — DETECTED_BUT_TOO_LATE
- ENS-EUR — ACTIVE_NOW — score mémoire 7.807/10 — sources V4 — DETECTED_BUT_TOO_LATE
- COW-EUR — MEMORY_24H — score mémoire 7.799/10 — sources V4 — MEMORY_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.773/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- G-EUR +54.99% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +43.80% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QKC-EUR +43.35% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- F-EUR +32.19% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SYN-EUR +27.08% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZAMA-EUR +23.04% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +22.85% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIG-EUR +21.03% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- S-EUR +20.70% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- INJ-EUR +19.41% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
