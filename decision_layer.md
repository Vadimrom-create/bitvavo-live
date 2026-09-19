# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T17:46:44.814496+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : SUI-EUR | action ACHETE_MAINTENANT | opportunité 8.769 | entrée 7.750 | trend 7.400 | rang 7.799
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : FET-EUR | action PLACE_LIMITE_PASSIVE | opportunité 9.028 | entrée 6.500 | trend 7.350 | rang 7.819
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : TAO-EUR | action LATENT_ACCELERATOR | opportunité 7.452 | entrée 4.500 | trend 8.050 | rang 7.069
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : KAS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.098 | entrée 6.500 | trend 8.950 | rang 7.856
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. KAS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.856
2. FET-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.819
3. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.799

## Accélération indépendante

- NEAR-EUR — BUILDING_ACCELERATION — score 5.073/10 — DETECTED_BUT_TOO_LATE
- EPIC-EUR — BUILDING_ACCELERATION — score 4.884/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- PEPE-EUR — ACTIVE_NOW — score mémoire 7.387/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- PROVE-EUR — ACTIVE_NOW — score mémoire 8.534/10 — sources V4 — WATCH_ONLY
- ATH-EUR — ACTIVE_NOW — score mémoire 8.351/10 — sources V4 — DETECTED_BUT_TOO_LATE
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.307/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 8.304/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- AERO-EUR — ACTIVE_NOW — score mémoire 8.022/10 — sources V4 — WATCH_ONLY
- ZIL-EUR — ACTIVE_NOW — score mémoire 7.964/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.907/10 — sources V4 — WATCH_ONLY
- PEAQ-EUR — ACTIVE_NOW — score mémoire 7.861/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VVV-EUR — ACTIVE_NOW — score mémoire 7.859/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZAMA-EUR +40.57% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +35.10% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- EPIC-EUR +33.25% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +29.89% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +21.96% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ENA-EUR +21.15% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CROSS-EUR +20.72% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FIL-EUR +20.45% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AVAX-EUR +19.98% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- STRK-EUR +17.38% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
