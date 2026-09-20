# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T12:52:13.446350+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AVAX-EUR | action ACHETE_MAINTENANT | opportunité 8.244 | entrée 6.950 | trend 8.150 | rang 7.223
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ENSO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.710 | entrée 6.250 | trend 8.750 | rang 6.748
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : ENA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.010 | entrée 7.600 | trend 8.500 | rang 7.586
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ENA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.586
2. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.553
3. EPIC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.278

## Accélération indépendante

- ZAMA-EUR — CONFIRMED_ACCELERATION — score 6.945/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- AVAX-EUR — ACTIVE_NOW — score mémoire 7.223/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- COTI-EUR — MEMORY_24H — score mémoire 7.904/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- LPT-EUR — ACTIVE_NOW — score mémoire 7.830/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- MERL-EUR — ACTIVE_NOW — score mémoire 7.815/10 — sources V4 — WATCH_ONLY
- BIGTIME-EUR — MEMORY_24H — score mémoire 7.662/10 — sources V4 — MEMORY_ONLY
- ENA-EUR — ACTIVE_NOW — score mémoire 7.586/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HYPE-EUR — ACTIVE_NOW — score mémoire 7.553/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.545/10 — sources V4 — WATCH_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 7.528/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- STX-EUR — ACTIVE_NOW — score mémoire 7.527/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CELR-EUR +73.67% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZAMA-EUR +18.82% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PTB-EUR +16.45% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ENSO-EUR +14.24% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- C-EUR +12.90% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CTSI-EUR +12.77% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- AVAX-EUR +11.98% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- S-EUR +8.89% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ACE-EUR +8.48% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SKL-EUR +8.35% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
