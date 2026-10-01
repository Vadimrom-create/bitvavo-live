# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-01T05:02:43.181070+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ENA-EUR | action ACHETE_MAINTENANT | opportunité 9.329 | entrée 7.650 | trend 8.400 | rang 8.101
  - V4 buy-ready with acceptable current entry; no structural veto. High extension/chase is retained as risk context, not an automatic veto.
- **MEILLEURE_LIMITE_PASSIVE** : XVG-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.759 | entrée 6.450 | trend 8.200 | rang 7.417
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ETHFI-EUR | action LATENT_ACCELERATOR | opportunité 7.656 | entrée 4.500 | trend 8.650 | rang 7.406
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ICP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.304 | entrée 6.400 | trend 8.700 | rang 8.406
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. ENA-EUR — ACHETE_MAINTENANT — rank 8.101 — opportunité 9.329 — entrée 7.650 — trend 8.400
2. AVAX-EUR — ACHETE_MAINTENANT — rank 7.896 — opportunité 8.146 — entrée 7.350 — trend 8.700
3. HBAR-EUR — ACHETE_MAINTENANT — rank 7.708 — opportunité 8.618 — entrée 7.200 — trend 8.150
4. NEAR-EUR — ACHETE_MAINTENANT — rank 7.677 — opportunité 8.169 — entrée 7.650 — trend 8.250
5. ADA-EUR — ACHETE_MAINTENANT — rank 7.386 — opportunité 8.870 — entrée 7.600 — trend 6.350
6. UNI-EUR — ACHETE_MAINTENANT — rank 6.654 — opportunité 7.808 — entrée 7.150 — trend 6.100
7. BTC-EUR — ACHETE_MAINTENANT — rank 6.416 — opportunité 8.047 — entrée 7.650 — trend 4.800

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ICP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.406
2. ENA-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.101
3. AVAX-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.896

## Accélération indépendante

- SYN-EUR — CONFIRMED_ACCELERATION — score 6.724/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PROMPT-EUR — BUILDING_ACCELERATION — score 5.942/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MOVR-EUR — BUILDING_ACCELERATION — score 5.916/10 — DETECTED_BUT_TOO_LATE
- AUDIO-EUR — BUILDING_ACCELERATION — score 5.902/10 — DETECTED_BUT_TOO_LATE
- MAGIC-EUR — BUILDING_ACCELERATION — score 5.414/10 — DETECTED_BUT_TOO_LATE
- USELESS-EUR — BUILDING_ACCELERATION — score 4.813/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BOB-EUR — BUILDING_ACCELERATION — score 4.801/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CT-EUR — MEMORY_24H — score mémoire 9.156/10 — sources ACCELERATION — MEMORY_ONLY
- CTR-EUR — MEMORY_24H — score mémoire 8.902/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ACU-EUR — MEMORY_24H — score mémoire 8.894/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ARPA-EUR — MEMORY_24H — score mémoire 8.595/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GLMR-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 8.406/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 8.400/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ENA-EUR — ACTIVE_NOW — score mémoire 8.101/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ICX-EUR — MEMORY_24H — score mémoire 8.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AVAX-EUR — ACTIVE_NOW — score mémoire 7.896/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- MOVR-EUR +72.33% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CT-EUR +47.03% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TRAC-EUR +29.76% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GLMR-EUR +27.94% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- STX-EUR +25.05% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MON-EUR +21.82% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CAP-EUR +17.43% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- PLUME-EUR +16.64% — DETECTED_EARLY — couche NONE — action NONE
- RED-EUR +14.06% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SAFE-EUR +12.64% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Gestion des positions détenues

Policy : STAGED_10_20_RUNNER_V1
- +10% : prise partielle 35%.
- +20% : seconde prise 35%.
- Runner conservé : 30%.
- Revue coût d'opportunité après 72 h ; sortie seulement avant la première partielle, proche/sous le PRU et avec momentum 15m affaibli.
- Pas de stop serré mécaniquement après une petite hausse ; le stop reste lié à l'invalidation structurelle.

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
