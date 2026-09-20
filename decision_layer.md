# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T19:04:28.024182+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HYPE-EUR | action ACHETE_MAINTENANT | opportunité 8.049 | entrée 7.250 | trend 8.500 | rang 7.820
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : WAL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.976 | entrée 6.950 | trend 8.700 | rang 7.804
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.820
2. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.804
3. ENSO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.450

## Accélération indépendante

- SAGA-EUR — BUILDING_ACCELERATION — score 5.721/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- PTB-EUR — MEMORY_24H — score mémoire 8.518/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- C-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 8.276/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 8.233/10 — sources V4 — WATCH_ONLY
- STX-EUR — ACTIVE_NOW — score mémoire 8.105/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- COW-EUR — ACTIVE_NOW — score mémoire 7.999/10 — sources V4 — WATCH_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 7.986/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- HYPE-EUR — ACTIVE_NOW — score mémoire 7.820/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.804/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- SUPER-EUR — ACTIVE_NOW — score mémoire 7.722/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SAGA-EUR +50.38% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CELR-EUR +34.28% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PTB-EUR +25.14% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FTT-EUR +19.14% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LUNA2-EUR +17.14% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +16.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +15.76% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- S-EUR +14.91% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AVA-EUR +14.40% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AVAX-EUR +13.93% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
