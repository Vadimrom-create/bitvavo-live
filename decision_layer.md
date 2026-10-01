# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-01T05:25:03.468836+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : NEAR-EUR | action ACHETE_MAINTENANT | opportunité 9.307 | entrée 7.800 | trend 8.250 | rang 8.190
  - V4 buy-ready with acceptable current entry; no structural veto. High extension/chase is retained as risk context, not an automatic veto.
- **MEILLEURE_LIMITE_PASSIVE** : KSM-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.447 | entrée 6.150 | trend 8.900 | rang 7.930
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : DIA-EUR | action LATENT_ACCELERATOR | opportunité 7.882 | entrée 5.600 | trend 8.750 | rang 7.591
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : HUMA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.141 | entrée 6.550 | trend 8.900 | rang 8.184
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. NEAR-EUR — ACHETE_MAINTENANT — rank 8.190 — opportunité 9.307 — entrée 7.800 — trend 8.250
2. AERO-EUR — ACHETE_MAINTENANT — rank 7.946 — opportunité 9.086 — entrée 7.650 — trend 7.750
3. AVAX-EUR — ACHETE_MAINTENANT — rank 7.904 — opportunité 8.102 — entrée 7.550 — trend 8.700
4. HBAR-EUR — ACHETE_MAINTENANT — rank 7.838 — opportunité 8.565 — entrée 7.150 — trend 8.150
5. ENA-EUR — ACHETE_MAINTENANT — rank 7.734 — opportunité 8.255 — entrée 7.400 — trend 8.400
6. TAO-EUR — ACHETE_MAINTENANT — rank 7.712 — opportunité 8.972 — entrée 7.700 — trend 7.050
7. RENDER-EUR — ACHETE_MAINTENANT — rank 7.621 — opportunité 8.558 — entrée 7.450 — trend 7.300
8. VIRTUAL-EUR — ACHETE_MAINTENANT — rank 7.510 — opportunité 8.449 — entrée 6.800 — trend 7.300
9. SOL-EUR — ACHETE_MAINTENANT — rank 7.198 — opportunité 8.684 — entrée 7.850 — trend 5.800
10. UNI-EUR — ACHETE_MAINTENANT — rank 7.064 — opportunité 8.350 — entrée 7.650 — trend 6.100
11. ADA-EUR — ACHETE_MAINTENANT — rank 6.974 — opportunité 7.971 — entrée 7.600 — trend 6.350
12. VET-EUR — ACHETE_MAINTENANT — rank 6.643 — opportunité 8.183 — entrée 7.300 — trend 5.950
13. MEGA-EUR — ACHETE_MAINTENANT — rank 6.503 — opportunité 8.051 — entrée 6.800 — trend 5.700
14. BTC-EUR — ACHETE_MAINTENANT — rank 6.458 — opportunité 8.047 — entrée 7.600 — trend 4.800

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. NEAR-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.190
2. HUMA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.184
3. AAVE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.033

## Accélération indépendante

- MOVR-EUR — CONFIRMED_ACCELERATION — score 8.346/10 — DETECTED_BUT_TOO_LATE
- JASMY-EUR — CONFIRMED_ACCELERATION — score 7.778/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRAC-EUR — CONFIRMED_ACCELERATION — score 7.579/10 — DETECTED_BUT_TOO_LATE
- MOVE-EUR — CONFIRMED_ACCELERATION — score 7.114/10 — DETECTED_BUT_TOO_LATE
- ICX-EUR — CONFIRMED_ACCELERATION — score 6.980/10 — DETECTED_BUT_TOO_LATE
- ESP-EUR — BUILDING_ACCELERATION — score 6.473/10 — DETECTED_BUT_TOO_LATE
- SOLV-EUR — BUILDING_ACCELERATION — score 6.390/10 — DETECTED_BUT_TOO_LATE
- FET-EUR — BUILDING_ACCELERATION — score 4.946/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SAFE-EUR — BUILDING_ACCELERATION — score 4.830/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- AERO-EUR — ACTIVE_NOW — score mémoire 7.946/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- MEGA-EUR — ACTIVE_NOW — score mémoire 6.503/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- CT-EUR — MEMORY_24H — score mémoire 9.156/10 — sources ACCELERATION — MEMORY_ONLY
- CTR-EUR — MEMORY_24H — score mémoire 8.902/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ACU-EUR — MEMORY_24H — score mémoire 8.894/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ARPA-EUR — MEMORY_24H — score mémoire 8.595/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GLMR-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 8.400/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MOVR-EUR — ACTIVE_NOW — score mémoire 8.346/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- NEAR-EUR — ACTIVE_NOW — score mémoire 8.190/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- MOVR-EUR +77.12% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CT-EUR +44.18% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GLMR-EUR +31.54% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- TRAC-EUR +27.26% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- STX-EUR +24.90% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MON-EUR +22.99% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CAP-EUR +18.84% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- PLUME-EUR +16.97% — DETECTED_EARLY — couche NONE — action NONE
- MOVE-EUR +15.18% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- RED-EUR +14.53% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
