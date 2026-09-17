# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-17T07:29:49.298687+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : NEAR-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.791 | entrée 6.750 | trend 8.100 | rang 7.171
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.171

## Accélération indépendante

- TREAD-EUR — BUILDING_ACCELERATION — score 6.121/10 — DETECTED_BUT_TOO_LATE
- SYN-EUR — BUILDING_ACCELERATION — score 5.931/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- KAS-EUR — ACTIVE_NOW — score mémoire 8.398/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 8.395/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- COTI-EUR — ACTIVE_NOW — score mémoire 8.216/10 — sources V4 — DETECTED_BUT_TOO_LATE
- PENDLE-EUR — ACTIVE_NOW — score mémoire 8.193/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ASTR-EUR — ACTIVE_NOW — score mémoire 8.173/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.153/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 8.122/10 — sources V4 — WATCH_ONLY
- TAO-EUR — ACTIVE_NOW — score mémoire 8.090/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 8.043/10 — sources V4 — WATCH_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 8.040/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- AVA-EUR +70.87% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FOLD-EUR +27.18% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- HNT-EUR +23.84% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SYN-EUR +23.28% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QUID-EUR +19.56% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- NEAR-EUR +17.39% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HEI-EUR +17.14% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PEAQ-EUR +14.57% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VVV-EUR +14.35% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- USELESS-EUR +13.58% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
