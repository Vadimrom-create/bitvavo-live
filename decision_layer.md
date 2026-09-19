# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T10:30:08.309414+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LINK-EUR | action ACHETE_MAINTENANT | opportunité 9.008 | entrée 7.800 | trend 6.950 | rang 7.699
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : SOL-EUR | action LATENT_ACCELERATOR | opportunité 7.581 | entrée 4.500 | trend 8.250 | rang 7.228
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : HYPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.090 | entrée 6.350 | trend 8.750 | rang 7.873
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.873
2. LINK-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.699
3. TAO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.653

## Accélération indépendante

- TAO-EUR — BUILDING_ACCELERATION — score 5.692/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- SYN-EUR — BUILDING_ACCELERATION — score 5.288/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- TAO-EUR — ACTIVE_NOW — score mémoire 7.653/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- PHA-EUR — ACTIVE_NOW — score mémoire 8.429/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- LPT-EUR — ACTIVE_NOW — score mémoire 8.306/10 — sources ACCELERATION, V4 — WATCH_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 8.287/10 — sources V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.226/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- OP-EUR — ACTIVE_NOW — score mémoire 8.122/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- LSK-EUR — MEMORY_24H — score mémoire 8.067/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 8.054/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ZRX-EUR — ACTIVE_NOW — score mémoire 7.962/10 — sources V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.959/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SYN-EUR +40.58% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- EDGE-EUR +36.14% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZAMA-EUR +32.98% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- HEI-EUR +29.14% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- F-EUR +28.87% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +28.34% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- XTZ-EUR +25.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- STRK-EUR +25.13% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIG-EUR +23.11% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +21.10% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
