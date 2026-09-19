# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T19:09:15.217189+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : SUI-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.177 | entrée 7.750 | trend 8.450 | rang 7.882
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. SUI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.882
2. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.831
3. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.519

## Accélération indépendante

- CNPY-EUR — CONFIRMED_ACCELERATION — score 7.809/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- EPIC-EUR — CONFIRMED_ACCELERATION — score 6.642/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- S-EUR — ACTIVE_NOW — score mémoire 8.364/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ROSE-EUR — ACTIVE_NOW — score mémoire 8.183/10 — sources V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.944/10 — sources V4 — WATCH_ONLY
- JUP-EUR — ACTIVE_NOW — score mémoire 7.923/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- LPT-EUR — ACTIVE_NOW — score mémoire 7.896/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SUI-EUR — ACTIVE_NOW — score mémoire 7.882/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- APT-EUR — ACTIVE_NOW — score mémoire 7.856/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- SENT-EUR — ACTIVE_NOW — score mémoire 7.834/10 — sources V4 — WATCH_ONLY
- HYPE-EUR — ACTIVE_NOW — score mémoire 7.831/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CNPY-EUR — ACTIVE_NOW — score mémoire 7.809/10 — sources ACCELERATION, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZAMA-EUR +47.28% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +39.09% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- EPIC-EUR +37.71% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +32.44% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- G-EUR +30.85% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +20.70% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ENA-EUR +19.93% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AVAX-EUR +18.01% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- INJ-EUR +17.94% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FIL-EUR +17.28% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
