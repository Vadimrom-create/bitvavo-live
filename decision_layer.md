# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-30T10:46:19.220236+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : XLM-EUR | action ACHETE_MAINTENANT | opportunité 8.262 | entrée 7.600 | trend 8.700 | rang 7.952
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ALICE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.304 | entrée 5.900 | trend 8.700 | rang 7.900
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : HUMA-EUR | action LATENT_ACCELERATOR | opportunité 7.831 | entrée 4.500 | trend 8.550 | rang 7.434
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ALGO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.372 | entrée 7.050 | trend 8.650 | rang 8.406
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. XLM-EUR — ACHETE_MAINTENANT — rank 7.952 — opportunité 8.262 — entrée 7.600 — trend 8.700
2. RENDER-EUR — ACHETE_MAINTENANT — rank 7.847 — opportunité 8.172 — entrée 8.050 — trend 8.150
3. WIF-EUR — ACHETE_MAINTENANT — rank 7.823 — opportunité 9.114 — entrée 7.250 — trend 7.550
4. CRV-EUR — ACHETE_MAINTENANT — rank 7.756 — opportunité 7.961 — entrée 6.950 — trend 8.650
5. NEAR-EUR — ACHETE_MAINTENANT — rank 7.739 — opportunité 9.135 — entrée 7.350 — trend 7.500
6. VIRTUAL-EUR — ACHETE_MAINTENANT — rank 7.680 — opportunité 8.837 — entrée 7.000 — trend 7.550
7. ADA-EUR — ACHETE_MAINTENANT — rank 7.259 — opportunité 7.956 — entrée 7.600 — trend 7.100

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ALGO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.406
2. COMP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.196
3. ICP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.103

## Accélération indépendante

- XMN-EUR — CONFIRMED_ACCELERATION — score 9.762/10 — DETECTED_BUT_TOO_LATE
- BTT-EUR — CONFIRMED_ACCELERATION — score 8.963/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRAC-EUR — CONFIRMED_ACCELERATION — score 8.468/10 — DETECTED_BUT_TOO_LATE
- ALT-EUR — CONFIRMED_ACCELERATION — score 7.671/10 — DETECTED_BUT_TOO_LATE
- NOM-EUR — CONFIRMED_ACCELERATION — score 6.570/10 — DETECTED_BUT_TOO_LATE
- RUNE-EUR — BUILDING_ACCELERATION — score 6.214/10 — DETECTED_BUT_TOO_LATE
- UMA-EUR — BUILDING_ACCELERATION — score 5.972/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NEO-EUR — BUILDING_ACCELERATION — score 5.416/10 — DETECTED_BUT_TOO_LATE
- FLOKI-EUR — BUILDING_ACCELERATION — score 5.272/10 — DETECTED_BUT_TOO_LATE
- FLOCK-EUR — BUILDING_ACCELERATION — score 5.085/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- XMN-EUR — ACTIVE_NOW — score mémoire 9.762/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- BTT-EUR — ACTIVE_NOW — score mémoire 8.963/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CTR-EUR — MEMORY_24H — score mémoire 8.902/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GWEI-EUR — MEMORY_24H — score mémoire 8.731/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TRAC-EUR — ACTIVE_NOW — score mémoire 8.468/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- WMTX-EUR — MEMORY_24H — score mémoire 8.460/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ALGO-EUR — ACTIVE_NOW — score mémoire 8.406/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LRC-EUR — MEMORY_24H — score mémoire 8.342/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AGI-EUR — MEMORY_24H — score mémoire 8.300/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- COMP-EUR — ACTIVE_NOW — score mémoire 8.196/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- MOVR-EUR +80.27% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CT-EUR +41.33% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- SOON-EUR +32.71% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GLMR-EUR +26.50% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- GTC-EUR +26.14% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARK-EUR +22.52% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PHA-EUR +21.53% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- TRAC-EUR +16.90% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- QNT-EUR +14.75% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZRO-EUR +13.29% — DETECTED_EARLY — couche NONE — action NONE

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
