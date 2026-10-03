# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-03T00:53:05.140831+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ALGO-EUR | action ACHETE_MAINTENANT | opportunité 9.211 | entrée 7.000 | trend 7.950 | rang 8.005
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : MAGIC-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.804 | entrée 5.850 | trend 8.650 | rang 7.595
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : INIT-EUR | action LATENT_ACCELERATOR | opportunité 7.540 | entrée 4.500 | trend 8.500 | rang 7.223
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AAVE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.520 | entrée 6.350 | trend 9.200 | rang 8.233
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. ALGO-EUR — ACHETE_MAINTENANT — rank 8.005 — opportunité 9.211 — entrée 7.000 — trend 7.950
2. SYRUP-EUR — ACHETE_MAINTENANT — rank 7.800 — opportunité 8.673 — entrée 6.950 — trend 8.200
3. WLD-EUR — ACHETE_MAINTENANT — rank 7.690 — opportunité 8.316 — entrée 7.150 — trend 8.450
4. LTC-EUR — ACHETE_MAINTENANT — rank 7.207 — opportunité 8.796 — entrée 7.250 — trend 6.600
5. AVAX-EUR — ACHETE_MAINTENANT — rank 7.156 — opportunité 8.801 — entrée 7.200 — trend 6.050

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. AAVE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.233
2. STX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.024
3. ALGO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.005

## Accélération indépendante

- MOVE-EUR — CONFIRMED_ACCELERATION — score 8.978/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CAP-EUR — CONFIRMED_ACCELERATION — score 7.453/10 — DETECTED_BUT_TOO_LATE
- NOT-EUR — CONFIRMED_ACCELERATION — score 7.031/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SOON-EUR — CONFIRMED_ACCELERATION — score 6.779/10 — DETECTED_BUT_TOO_LATE
- SWEAT-EUR — CONFIRMED_ACCELERATION — score 6.660/10 — DETECTED_BUT_TOO_LATE
- PUMP-EUR — BUILDING_ACCELERATION — score 6.496/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZEUS-EUR — BUILDING_ACCELERATION — score 5.889/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRAC-EUR — BUILDING_ACCELERATION — score 5.825/10 — DETECTED_BUT_TOO_LATE
- SAND-EUR — BUILDING_ACCELERATION — score 5.819/10 — DETECTED_BUT_TOO_LATE
- CT-EUR — BUILDING_ACCELERATION — score 5.403/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- SUI-EUR — ACTIVE_NOW — score mémoire 6.534/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- EDGE-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FOLD-EUR — MEMORY_24H — score mémoire 9.866/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PEOPLE-EUR — MEMORY_24H — score mémoire 9.036/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MOVE-EUR — ACTIVE_NOW — score mémoire 8.978/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- GNS-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.233/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SOSO-EUR — MEMORY_24H — score mémoire 8.156/10 — sources ACCELERATION — MEMORY_ONLY
- STX-EUR — ACTIVE_NOW — score mémoire 8.024/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ALGO-EUR — ACTIVE_NOW — score mémoire 8.005/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SAND-EUR +51.45% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GALA-EUR +17.87% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ATH-EUR +13.17% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENJ-EUR +13.08% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- APE-EUR +12.50% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CAP-EUR +11.74% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MANA-EUR +10.87% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- WLD-EUR +10.65% — DETECTED_EARLY — couche NONE — action NONE
- PYTH-EUR +9.43% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- SPK-EUR +9.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION

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
