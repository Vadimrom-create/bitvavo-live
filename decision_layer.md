# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T20:35:19.326803+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : WLD-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.940 | entrée 6.950 | trend 8.150 | rang 7.363
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. WLD-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.363
2. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.846
3. UNI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.422

## Accélération indépendante

- STRK-EUR — CONFIRMED_ACCELERATION — score 7.519/10 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — BUILDING_ACCELERATION — score 5.429/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- LDO-EUR — ACTIVE_NOW — score mémoire 8.140/10 — sources V4 — WATCH_ONLY
- METIS-EUR — ACTIVE_NOW — score mémoire 8.020/10 — sources V4 — DETECTED_BUT_TOO_LATE
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.001/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.946/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- NEO-EUR — ACTIVE_NOW — score mémoire 7.876/10 — sources V4 — WATCH_ONLY
- FORM-EUR — ACTIVE_NOW — score mémoire 7.861/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.807/10 — sources V4 — WATCH_ONLY
- GRT-EUR — ACTIVE_NOW — score mémoire 7.744/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.728/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ATOM-EUR — ACTIVE_NOW — score mémoire 7.688/10 — sources V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- G-EUR +56.18% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +52.68% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- F-EUR +38.72% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARB-EUR +27.16% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- APT-EUR +25.45% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +22.78% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZAMA-EUR +21.28% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- S-EUR +20.76% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MET-EUR +20.46% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- C-EUR +19.95% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
