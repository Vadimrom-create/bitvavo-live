# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T23:36:32.897419+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HYPE-EUR | action ACHETE_MAINTENANT | opportunité 8.413 | entrée 7.850 | trend 8.400 | rang 7.953
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : PEPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.963 | entrée 6.950 | trend 8.950 | rang 7.943
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.953
2. PEPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.943

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- VTHO-EUR — MEMORY_24H — score mémoire 8.268/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GRT-EUR — ACTIVE_NOW — score mémoire 8.162/10 — sources V4 — WATCH_ONLY
- VVV-EUR — ACTIVE_NOW — score mémoire 8.022/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ROSE-EUR — ACTIVE_NOW — score mémoire 7.994/10 — sources V4 — WATCH_ONLY
- HYPE-EUR — ACTIVE_NOW — score mémoire 7.953/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- YB-EUR — MEMORY_24H — score mémoire 7.953/10 — sources V4 — MEMORY_ONLY
- PEPE-EUR — ACTIVE_NOW — score mémoire 7.943/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FET-EUR — ACTIVE_NOW — score mémoire 7.864/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 7.861/10 — sources ACCELERATION, V4 — WATCH_ONLY
- SSV-EUR — ACTIVE_NOW — score mémoire 7.828/10 — sources V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- F-EUR +66.94% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +59.66% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +52.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- C-EUR +26.91% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARB-EUR +24.41% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIG-EUR +22.26% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- APT-EUR +21.49% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZK-EUR +21.01% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- RAY-EUR +20.63% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +20.04% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
