# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T23:47:21.737148+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HYPE-EUR | action ACHETE_MAINTENANT | opportunité 7.848 | entrée 7.550 | trend 8.400 | rang 7.670
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : PEPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.902 | entrée 7.350 | trend 8.950 | rang 7.968
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. PEPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.968
2. HYPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.670

## Accélération indépendante

- SYN-EUR — CONFIRMED_ACCELERATION — score 8.311/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- SYN-EUR — ACTIVE_NOW — score mémoire 8.311/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- VTHO-EUR — MEMORY_24H — score mémoire 8.268/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GRT-EUR — ACTIVE_NOW — score mémoire 8.143/10 — sources V4 — WATCH_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 7.976/10 — sources V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 7.975/10 — sources ACCELERATION, V4 — WATCH_ONLY
- PEPE-EUR — ACTIVE_NOW — score mémoire 7.968/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- YB-EUR — MEMORY_24H — score mémoire 7.953/10 — sources V4 — MEMORY_ONLY
- AERO-EUR — MEMORY_24H — score mémoire 7.882/10 — sources V4 — MEMORY_ONLY
- ROSE-EUR — ACTIVE_NOW — score mémoire 7.874/10 — sources V4 — WATCH_ONLY
- SSV-EUR — ACTIVE_NOW — score mémoire 7.866/10 — sources V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- F-EUR +64.23% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +59.19% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +51.60% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARB-EUR +26.61% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- C-EUR +24.64% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZIG-EUR +22.23% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- APT-EUR +21.88% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZK-EUR +21.01% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- RAY-EUR +19.75% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- S-EUR +19.22% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
