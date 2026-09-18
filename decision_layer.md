# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T23:41:49.748080+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HYPE-EUR | action ACHETE_MAINTENANT | opportunité 8.205 | entrée 7.600 | trend 8.400 | rang 7.835
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : PEPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.988 | entrée 7.350 | trend 8.950 | rang 8.004
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. PEPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.004
2. HYPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.835

## Accélération indépendante

- SYN-EUR — CONFIRMED_ACCELERATION — score 6.913/10 — DETECTED_BUT_TOO_LATE
- STRK-EUR — BUILDING_ACCELERATION — score 6.376/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- VTHO-EUR — MEMORY_24H — score mémoire 8.268/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GRT-EUR — ACTIVE_NOW — score mémoire 8.145/10 — sources V4 — WATCH_ONLY
- VVV-EUR — ACTIVE_NOW — score mémoire 8.050/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- PEPE-EUR — ACTIVE_NOW — score mémoire 8.004/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ROSE-EUR — ACTIVE_NOW — score mémoire 7.990/10 — sources V4 — WATCH_ONLY
- YB-EUR — MEMORY_24H — score mémoire 7.953/10 — sources V4 — MEMORY_ONLY
- FET-EUR — ACTIVE_NOW — score mémoire 7.886/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.882/10 — sources V4 — WATCH_ONLY
- W-EUR — ACTIVE_NOW — score mémoire 7.841/10 — sources V4 — DETECTED_BUT_TOO_LATE
- SSV-EUR — ACTIVE_NOW — score mémoire 7.837/10 — sources V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- F-EUR +64.79% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +59.91% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +52.09% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARB-EUR +26.16% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- C-EUR +25.10% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- APT-EUR +22.32% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIG-EUR +22.16% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZK-EUR +21.01% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- SYN-EUR +20.02% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- S-EUR +19.22% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
