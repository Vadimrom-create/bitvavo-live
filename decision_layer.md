# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T17:33:46.004652+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : SUI-EUR | action ACHETE_MAINTENANT | opportunité 8.772 | entrée 8.000 | trend 7.400 | rang 7.804
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : TAO-EUR | action LATENT_ACCELERATOR | opportunité 7.462 | entrée 4.500 | trend 8.050 | rang 7.056
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : PEPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.051 | entrée 6.600 | trend 8.450 | rang 7.217
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. SUI-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.804
2. ADA-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.404
3. PEPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.217

## Accélération indépendante

- EPIC-EUR — CONFIRMED_ACCELERATION — score 8.916/10 — DETECTED_BUT_TOO_LATE
- INJ-EUR — BUILDING_ACCELERATION — score 5.049/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- EPIC-EUR — ACTIVE_NOW — score mémoire 8.916/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- PROVE-EUR — ACTIVE_NOW — score mémoire 8.537/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 8.259/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.153/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ATH-EUR — ACTIVE_NOW — score mémoire 8.107/10 — sources V4 — DETECTED_BUT_TOO_LATE
- ZIL-EUR — ACTIVE_NOW — score mémoire 7.986/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.962/10 — sources V4 — WATCH_ONLY
- SENT-EUR — ACTIVE_NOW — score mémoire 7.919/10 — sources V4 — WATCH_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.904/10 — sources V4 — WATCH_ONLY
- LPT-EUR — ACTIVE_NOW — score mémoire 7.820/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZAMA-EUR +38.01% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +37.15% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- EPIC-EUR +30.41% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +28.79% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENA-EUR +22.48% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FIL-EUR +21.17% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AVAX-EUR +20.69% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- CROSS-EUR +20.00% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +19.24% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ALLO-EUR +17.88% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
