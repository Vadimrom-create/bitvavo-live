# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-02T03:04:20.054103+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AAVE-EUR | action ACHETE_MAINTENANT | opportunité 8.214 | entrée 7.450 | trend 8.950 | rang 8.061
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : EPIC-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.556 | entrée 5.850 | trend 8.200 | rang 7.329
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : PROM-EUR | action LATENT_ACCELERATOR | opportunité 7.695 | entrée 5.350 | trend 8.150 | rang 7.356
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : STX-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.490 | entrée 6.900 | trend 8.650 | rang 8.030
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. AAVE-EUR — ACHETE_MAINTENANT — rank 8.061 — opportunité 8.214 — entrée 7.450 — trend 8.950
2. SUI-EUR — ACHETE_MAINTENANT — rank 7.667 — opportunité 8.914 — entrée 7.850 — trend 6.800
3. HBAR-EUR — ACHETE_MAINTENANT — rank 7.544 — opportunité 8.033 — entrée 7.200 — trend 7.950
4. TAO-EUR — ACHETE_MAINTENANT — rank 7.370 — opportunité 8.623 — entrée 7.600 — trend 6.550
5. DOT-EUR — ACHETE_MAINTENANT — rank 7.183 — opportunité 8.546 — entrée 7.000 — trend 6.550
6. ADA-EUR — ACHETE_MAINTENANT — rank 7.175 — opportunité 8.171 — entrée 7.450 — trend 6.600
7. XPL-EUR — ACHETE_MAINTENANT — rank 6.955 — opportunité 8.636 — entrée 7.450 — trend 5.450
8. WIF-EUR — ACHETE_MAINTENANT — rank 6.938 — opportunité 8.221 — entrée 7.100 — trend 6.250

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. AAVE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.061
2. STX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.030
3. DYDX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.893

## Accélération indépendante

- ICX-EUR — CONFIRMED_ACCELERATION — score 9.062/10 — DETECTED_BUT_TOO_LATE
- TRAC-EUR — CONFIRMED_ACCELERATION — score 7.338/10 — DETECTED_BUT_TOO_LATE
- ZAMA-EUR — CONFIRMED_ACCELERATION — score 6.896/10 — DETECTED_BUT_TOO_LATE
- SCR-EUR — BUILDING_ACCELERATION — score 5.937/10 — DETECTED_BUT_TOO_LATE
- FET-EUR — BUILDING_ACCELERATION — score 5.849/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RPL-EUR — BUILDING_ACCELERATION — score 5.733/10 — DETECTED_BUT_TOO_LATE
- PEAQ-EUR — BUILDING_ACCELERATION — score 5.460/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ORCA-EUR — BUILDING_ACCELERATION — score 5.151/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- KAS-EUR — BUILDING_ACCELERATION — score 5.058/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- VIRTUAL-EUR — BUILDING_ACCELERATION — score 4.913/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- CPOOL-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- POND-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICX-EUR — ACTIVE_NOW — score mémoire 9.062/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- ZRC-EUR — MEMORY_24H — score mémoire 8.847/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- OSMO-EUR — MEMORY_24H — score mémoire 8.342/10 — sources ACCELERATION — MEMORY_ONLY
- AGI-EUR — MEMORY_24H — score mémoire 8.119/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.061/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- STX-EUR — ACTIVE_NOW — score mémoire 8.030/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.002/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DYDX-EUR — ACTIVE_NOW — score mémoire 7.893/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SWEAT-EUR +143.81% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- GTC-EUR +79.87% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CT-EUR +26.96% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SCR-EUR +26.74% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MEGA-EUR +21.77% — DETECTED_EARLY — couche NONE — action NONE
- MOVR-EUR +21.03% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +19.48% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SUPER-EUR +18.06% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ALICE-EUR +17.01% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NOM-EUR +16.68% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
