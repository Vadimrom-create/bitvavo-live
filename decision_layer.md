# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T08:19:46.541322+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : NEAR-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.707 | entrée 7.250 | trend 7.950 | rang 7.614
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.614
2. INJ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.443
3. STRK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.249

## Accélération indépendante

- STRK-EUR — CONFIRMED_ACCELERATION — score 6.727/10 — DETECTED_BUT_TOO_LATE
- NPC-EUR — BUILDING_ACCELERATION — score 5.915/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- NEAR-EUR — BUILDING_ACCELERATION — score 5.754/10 — DETECTED_BUT_TOO_LATE
- ENA-EUR — BUILDING_ACCELERATION — score 4.936/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- AERO-EUR — ACTIVE_NOW — score mémoire 8.226/10 — sources V4 — WATCH_ONLY
- APT-EUR — ACTIVE_NOW — score mémoire 8.073/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- VVV-EUR — ACTIVE_NOW — score mémoire 8.059/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ZK-EUR — ACTIVE_NOW — score mémoire 8.032/10 — sources V4 — DETECTED_BUT_TOO_LATE
- KAS-EUR — ACTIVE_NOW — score mémoire 7.856/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 7.819/10 — sources V4 — WATCH_ONLY
- S-EUR — ACTIVE_NOW — score mémoire 7.749/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.738/10 — sources V4 — WATCH_ONLY
- COW-EUR — ACTIVE_NOW — score mémoire 7.717/10 — sources V4 — WATCH_ONLY
- W-EUR — ACTIVE_NOW — score mémoire 7.704/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CELR-EUR +79.69% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZIL-EUR +29.38% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZAMA-EUR +19.41% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- T-EUR +17.40% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SKL-EUR +17.24% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- C-EUR +16.93% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CTSI-EUR +15.11% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SOLV-EUR +13.40% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ONG-EUR +12.83% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- JTO-EUR +11.83% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
