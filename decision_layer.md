# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T03:38:11.949041+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : TAO-EUR | action ACHETE_MAINTENANT | opportunité 8.905 | entrée 7.400 | trend 6.500 | rang 7.394
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : HYPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.915 | entrée 8.250 | trend 8.250 | rang 7.759
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.759
2. TAO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.394
3. APT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.388

## Accélération indépendante

- SYN-EUR — BUILDING_ACCELERATION — score 6.189/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- TAO-EUR — ACTIVE_NOW — score mémoire 7.394/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- VTHO-EUR — MEMORY_24H — score mémoire 8.268/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PEPE-EUR — MEMORY_24H — score mémoire 8.255/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.240/10 — sources ACCELERATION, V4 — WATCH_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 8.120/10 — sources V4 — WATCH_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 8.111/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LTC-EUR — ACTIVE_NOW — score mémoire 7.935/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- TIA-EUR — ACTIVE_NOW — score mémoire 7.759/10 — sources V4 — WATCH_ONLY
- HYPE-EUR — ACTIVE_NOW — score mémoire 7.759/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.755/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- G-EUR +69.14% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +42.17% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- F-EUR +35.54% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SYN-EUR +25.69% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- XTZ-EUR +24.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FOLD-EUR +20.56% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZIG-EUR +19.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QKC-EUR +19.43% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZAMA-EUR +18.92% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- INJ-EUR +17.15% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
