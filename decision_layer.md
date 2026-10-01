# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-01T17:57:43.240820+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AAVE-EUR | action ACHETE_MAINTENANT | opportunité 9.104 | entrée 7.450 | trend 8.700 | rang 8.264
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : DIA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.163 | entrée 6.150 | trend 8.750 | rang 7.838
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : KSM-EUR | action LATENT_ACCELERATOR | opportunité 8.018 | entrée 5.200 | trend 9.200 | rang 7.820
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : STX-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.141 | entrée 6.450 | trend 9.200 | rang 7.944
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. AAVE-EUR — ACHETE_MAINTENANT — rank 8.264 — opportunité 9.104 — entrée 7.450 — trend 8.700
2. ZRO-EUR — ACHETE_MAINTENANT — rank 8.203 — opportunité 8.901 — entrée 7.450 — trend 8.900
3. GALA-EUR — ACHETE_MAINTENANT — rank 8.186 — opportunité 9.288 — entrée 6.900 — trend 8.450
4. AVAX-EUR — ACHETE_MAINTENANT — rank 8.165 — opportunité 8.892 — entrée 7.150 — trend 8.450
5. SUI-EUR — ACHETE_MAINTENANT — rank 7.933 — opportunité 9.214 — entrée 7.600 — trend 7.900
6. PUMP-EUR — ACHETE_MAINTENANT — rank 7.412 — opportunité 8.874 — entrée 7.150 — trend 8.000
7. RENDER-EUR — ACHETE_MAINTENANT — rank 7.347 — opportunité 8.867 — entrée 7.500 — trend 6.400
8. XLM-EUR — ACHETE_MAINTENANT — rank 6.782 — opportunité 8.200 — entrée 7.450 — trend 5.950
9. ETH-EUR — ACHETE_MAINTENANT — rank 6.653 — opportunité 8.389 — entrée 7.600 — trend 5.100

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. AAVE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.264
2. ZRO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.203
3. GALA-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.186

## Accélération indépendante

- INIT-EUR — CONFIRMED_ACCELERATION — score 8.067/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SWEAT-EUR — CONFIRMED_ACCELERATION — score 7.050/10 — DETECTED_BUT_TOO_LATE
- PONKE-EUR — BUILDING_ACCELERATION — score 6.257/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CETUS-EUR — BUILDING_ACCELERATION — score 5.819/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- KAT-EUR — BUILDING_ACCELERATION — score 5.505/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PUMP-EUR — BUILDING_ACCELERATION — score 5.410/10 — DETECTED_BUT_TOO_LATE
- MAGIC-EUR — BUILDING_ACCELERATION — score 4.938/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- AAVE-EUR — ACTIVE_NOW — score mémoire 8.264/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- SUI-EUR — ACTIVE_NOW — score mémoire 7.933/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- CPOOL-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GRASS-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MOVR-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CT-EUR — MEMORY_24H — score mémoire 8.691/10 — sources ACCELERATION — MEMORY_ONLY
- CHILLGUY-EUR — MEMORY_24H — score mémoire 8.548/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ARK-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- OSMO-EUR — MEMORY_24H — score mémoire 8.342/10 — sources ACCELERATION — MEMORY_ONLY
- ARPA-EUR — MEMORY_DECAY_24_72H — score mémoire 8.237/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- SWEAT-EUR +151.28% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- MOVR-EUR +71.66% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CAP-EUR +33.38% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- CT-EUR +28.12% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ALICE-EUR +28.12% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MEGA-EUR +27.03% — DETECTED_EARLY — couche NONE — action NONE
- SYN-EUR +22.46% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NOS-EUR +20.99% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MON-EUR +20.88% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GTC-EUR +15.08% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
