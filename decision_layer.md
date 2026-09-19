# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T18:53:43.272509+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : SUI-EUR | action ACHETE_MAINTENANT | opportunité 7.787 | entrée 7.350 | trend 8.450 | rang 7.672
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : HYPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.987 | entrée 6.850 | trend 8.750 | rang 7.886
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.886
2. SUI-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.672
3. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.442

## Accélération indépendante

- CNPY-EUR — BUILDING_ACCELERATION — score 5.547/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- ZAMA-EUR — BUILDING_ACCELERATION — score 4.807/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- S-EUR — ACTIVE_NOW — score mémoire 8.364/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ROSE-EUR — ACTIVE_NOW — score mémoire 8.237/10 — sources V4 — WATCH_ONLY
- LPT-EUR — ACTIVE_NOW — score mémoire 7.902/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- TRB-EUR — ACTIVE_NOW — score mémoire 7.890/10 — sources V4 — WATCH_ONLY
- HYPE-EUR — ACTIVE_NOW — score mémoire 7.886/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SENT-EUR — ACTIVE_NOW — score mémoire 7.877/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.851/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- STX-EUR — ACTIVE_NOW — score mémoire 7.833/10 — sources V4 — DETECTED_BUT_TOO_LATE
- JUP-EUR — ACTIVE_NOW — score mémoire 7.829/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 7.824/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZAMA-EUR +49.21% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +37.47% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +32.22% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +30.83% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +29.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +21.56% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ENA-EUR +21.41% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FIL-EUR +19.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AVAX-EUR +18.41% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- CROSS-EUR +18.14% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
