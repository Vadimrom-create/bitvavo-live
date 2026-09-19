# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T03:21:42.794589+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : TAO-EUR | action ACHETE_MAINTENANT | opportunité 8.654 | entrée 7.200 | trend 6.500 | rang 7.209
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : HYPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.130 | entrée 7.850 | trend 8.250 | rang 7.784
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.784
2. SOL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.391
3. APT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.320

## Accélération indépendante

- SYN-EUR — BUILDING_ACCELERATION — score 5.306/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- TAO-EUR — ACTIVE_NOW — score mémoire 7.209/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.335/10 — sources ACCELERATION, V4 — WATCH_ONLY
- VTHO-EUR — MEMORY_24H — score mémoire 8.268/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PEPE-EUR — MEMORY_24H — score mémoire 8.255/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 8.245/10 — sources V4 — WATCH_ONLY
- BEAM-EUR — ACTIVE_NOW — score mémoire 7.904/10 — sources V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.883/10 — sources V4 — WATCH_ONLY
- COW-EUR — MEMORY_24H — score mémoire 7.799/10 — sources V4 — MEMORY_ONLY
- HYPE-EUR — ACTIVE_NOW — score mémoire 7.784/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 7.771/10 — sources V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- G-EUR +74.90% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +40.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- F-EUR +34.45% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- XTZ-EUR +24.20% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QKC-EUR +23.15% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SYN-EUR +22.60% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FOLD-EUR +20.25% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZAMA-EUR +20.23% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- S-EUR +19.87% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIG-EUR +19.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
