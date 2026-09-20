# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T09:38:33.254132+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ONDO-EUR | action ACHETE_MAINTENANT | opportunité 8.948 | entrée 7.250 | trend 7.000 | rang 7.524
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : ENA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.353 | entrée 7.250 | trend 8.500 | rang 7.841
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ENA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.841
2. ONDO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.524
3. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.310

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- KAS-EUR — ACTIVE_NOW — score mémoire 8.201/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- RAY-EUR — ACTIVE_NOW — score mémoire 7.974/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- COTI-EUR — ACTIVE_NOW — score mémoire 7.904/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.889/10 — sources V4 — WATCH_ONLY
- ENA-EUR — ACTIVE_NOW — score mémoire 7.841/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.833/10 — sources V4 — WATCH_ONLY
- MERL-EUR — ACTIVE_NOW — score mémoire 7.777/10 — sources V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.715/10 — sources V4 — WATCH_ONLY
- SENT-EUR — ACTIVE_NOW — score mémoire 7.666/10 — sources V4 — WATCH_ONLY
- BIGTIME-EUR — MEMORY_24H — score mémoire 7.662/10 — sources V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- CELR-EUR +76.91% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZIL-EUR +26.94% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CTSI-EUR +17.68% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SKL-EUR +17.23% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- JTO-EUR +13.09% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- T-EUR +11.96% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SOLV-EUR +10.34% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AVAX-EUR +9.99% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ENA-EUR +9.94% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- STX-EUR +9.91% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
