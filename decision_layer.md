# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-28T23:33:50.515089+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : VIRTUAL-EUR | action ACHETE_MAINTENANT | opportunité 8.775 | entrée 7.200 | trend 9.000 | rang 8.222
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : AZTEC-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.831 | entrée 5.800 | trend 8.400 | rang 7.460
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : MIOTA-EUR | action LATENT_ACCELERATOR | opportunité 7.812 | entrée 5.400 | trend 8.900 | rang 7.521
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : W-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.388 | entrée 7.150 | trend 8.650 | rang 7.964
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. VIRTUAL-EUR — ACHETE_MAINTENANT — rank 8.222 — opportunité 8.775 — entrée 7.200 — trend 9.000
2. XLM-EUR — ACHETE_MAINTENANT — rank 7.994 — opportunité 8.298 — entrée 7.300 — trend 8.800
3. XDC-EUR — ACHETE_MAINTENANT — rank 7.969 — opportunité 8.016 — entrée 7.250 — trend 9.000
4. ETC-EUR — ACHETE_MAINTENANT — rank 7.595 — opportunité 8.591 — entrée 7.350 — trend 7.400
5. RENDER-EUR — ACHETE_MAINTENANT — rank 7.542 — opportunité 8.344 — entrée 7.500 — trend 7.850

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. VIRTUAL-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.222
2. XLM-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.994
3. XDC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.969

## Accélération indépendante

- CRV-EUR — CONFIRMED_ACCELERATION — score 9.394/10 — DETECTED_BUT_TOO_LATE
- PEOPLE-EUR — CONFIRMED_ACCELERATION — score 6.896/10 — DETECTED_BUT_TOO_LATE
- RLC-EUR — CONFIRMED_ACCELERATION — score 6.800/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CELO-EUR — BUILDING_ACCELERATION — score 6.008/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LUMIA-EUR — BUILDING_ACCELERATION — score 5.762/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CYBER-EUR — BUILDING_ACCELERATION — score 5.625/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TOSHI-EUR — BUILDING_ACCELERATION — score 5.193/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BILL-EUR — BUILDING_ACCELERATION — score 5.058/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PNUT-EUR — BUILDING_ACCELERATION — score 5.002/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- VIRTUAL-EUR — ACTIVE_NOW — score mémoire 8.222/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- CRV-EUR — ACTIVE_NOW — score mémoire 9.394/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ZRC-EUR — MEMORY_24H — score mémoire 9.275/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PUFFER-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 8.844/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- XLM-EUR — ACTIVE_NOW — score mémoire 7.994/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- XDC-EUR — ACTIVE_NOW — score mémoire 7.969/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- W-EUR — ACTIVE_NOW — score mémoire 7.964/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LINK-EUR — ACTIVE_NOW — score mémoire 7.929/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ARX-EUR — ACTIVE_NOW — score mémoire 7.813/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- NMR-EUR +44.99% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HBAR-EUR +27.41% — DETECTED_EARLY — couche NONE — action NONE
- ALGO-EUR +13.08% — DETECTED_EARLY — couche NONE — action NONE
- LINK-EUR +10.12% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- 0G-EUR +9.88% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- IKA-EUR +9.73% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- CRV-EUR +9.06% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MIOTA-EUR +8.80% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AZTEC-EUR +6.91% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- XLM-EUR +6.16% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
