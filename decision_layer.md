# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T03:01:51.375267+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ONDO-EUR | action ACHETE_MAINTENANT | opportunité 8.735 | entrée 7.150 | trend 7.650 | rang 7.750
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : HYPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.984 | entrée 7.350 | trend 8.250 | rang 7.650
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ONDO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.750
2. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.650
3. ADA-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.243

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- ONDO-EUR — ACTIVE_NOW — score mémoire 7.750/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ADA-EUR — ACTIVE_NOW — score mémoire 7.243/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- SYN-EUR — MEMORY_24H — score mémoire 8.620/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 8.460/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — MEMORY_24H — score mémoire 8.268/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PEPE-EUR — MEMORY_24H — score mémoire 8.255/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- BEAM-EUR — ACTIVE_NOW — score mémoire 8.213/10 — sources V4 — WATCH_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 8.143/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.062/10 — sources ACCELERATION, V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.888/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- G-EUR +52.57% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +43.87% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- F-EUR +35.22% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- XTZ-EUR +25.33% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZAMA-EUR +21.93% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +21.62% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- S-EUR +20.68% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QKC-EUR +20.62% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZIG-EUR +19.95% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MORPHO-EUR +17.35% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
