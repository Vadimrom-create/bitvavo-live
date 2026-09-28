# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-28T01:11:18.374068+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : EIGEN-EUR | action ACHETE_MAINTENANT | opportunité 9.241 | entrée 7.100 | trend 8.900 | rang 8.534
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : LDO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.008 | entrée 5.950 | trend 8.950 | rang 7.765
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BIGTIME-EUR | action LATENT_ACCELERATOR | opportunité 8.628 | entrée 5.750 | trend 8.900 | rang 8.061
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : SUI-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.516 | entrée 7.850 | trend 8.850 | rang 7.983
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. EIGEN-EUR — ACHETE_MAINTENANT — rank 8.534 — opportunité 9.241 — entrée 7.100 — trend 8.900
2. RENDER-EUR — ACHETE_MAINTENANT — rank 8.217 — opportunité 8.277 — entrée 7.150 — trend 9.200
3. DOT-EUR — ACHETE_MAINTENANT — rank 8.082 — opportunité 8.166 — entrée 7.200 — trend 8.950
4. LINK-EUR — ACHETE_MAINTENANT — rank 8.057 — opportunité 8.316 — entrée 7.250 — trend 8.700
5. GMT-EUR — ACHETE_MAINTENANT — rank 8.045 — opportunité 8.418 — entrée 6.900 — trend 8.750
6. HBAR-EUR — ACHETE_MAINTENANT — rank 8.034 — opportunité 9.168 — entrée 7.600 — trend 7.700
7. PYTH-EUR — ACHETE_MAINTENANT — rank 7.868 — opportunité 8.501 — entrée 7.050 — trend 8.850
8. TRX-EUR — ACHETE_MAINTENANT — rank 6.058 — opportunité 8.042 — entrée 7.500 — trend 3.900

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. EIGEN-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.534
2. RENDER-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.217
3. DOT-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.082

## Accélération indépendante

- ELSA-EUR — CONFIRMED_ACCELERATION — score 9.531/10 — DETECTED_BUT_TOO_LATE
- OSMO-EUR — CONFIRMED_ACCELERATION — score 6.624/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TAI-EUR — BUILDING_ACCELERATION — score 6.116/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MOCA-EUR — BUILDING_ACCELERATION — score 5.558/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- DGB-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ELSA-EUR — ACTIVE_NOW — score mémoire 9.531/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- EIGEN-EUR — ACTIVE_NOW — score mémoire 8.534/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- YB-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- QNT-EUR — MEMORY_24H — score mémoire 8.429/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FRAX-EUR — MEMORY_24H — score mémoire 8.380/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- RENDER-EUR — ACTIVE_NOW — score mémoire 8.217/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ACX-EUR — MEMORY_24H — score mémoire 8.120/10 — sources ACCELERATION — MEMORY_ONLY
- DOT-EUR — ACTIVE_NOW — score mémoire 8.082/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- QNT-EUR +62.17% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOON-EUR +36.35% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +28.88% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- INX-EUR +28.37% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRT-EUR +26.64% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- IRYS-EUR +18.76% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- SEI-EUR +17.57% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PUMP-EUR +16.68% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- W-EUR +15.29% — DETECTED_EARLY — couche NONE — action NONE
- IMX-EUR +14.49% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
