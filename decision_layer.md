# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-13T14:33:44.868325+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : TAO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.406 | entrée 7.200 | trend 7.650 | rang 7.611
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.611

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- LDO-EUR — ACTIVE_NOW — score mémoire 8.245/10 — sources V4 — WATCH_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 8.151/10 — sources V4 — WATCH_ONLY
- ATOM-EUR — ACTIVE_NOW — score mémoire 8.112/10 — sources V4 — DETECTED_BUT_TOO_LATE
- PROM-EUR — ACTIVE_NOW — score mémoire 8.073/10 — sources V4 — WATCH_ONLY
- SYRUP-EUR — ACTIVE_NOW — score mémoire 7.980/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.949/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.896/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- DOT-EUR — ACTIVE_NOW — score mémoire 7.796/10 — sources V4 — DETECTED_BUT_TOO_LATE
- CHILLGUY-EUR — ACTIVE_NOW — score mémoire 7.775/10 — sources V4 — DETECTED_BUT_TOO_LATE
- KAS-EUR — ACTIVE_NOW — score mémoire 7.756/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- LSK-EUR +248.44% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CVC-EUR +82.55% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PUNDIX-EUR +38.84% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARK-EUR +28.96% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GLM-EUR +18.87% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- STRAX-EUR +17.01% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- POWR-EUR +16.23% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- REZ-EUR +14.58% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KNC-EUR +13.49% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VTHO-EUR +13.32% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
