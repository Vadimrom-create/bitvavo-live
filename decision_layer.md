# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-01T12:38:28.503270+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ALGO-EUR | action ACHETE_MAINTENANT | opportunité 8.804 | entrée 6.850 | trend 8.150 | rang 7.995
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : HUMA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.078 | entrée 5.800 | trend 8.850 | rang 7.635
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : REZ-EUR | action LATENT_ACCELERATOR | opportunité 7.852 | entrée 5.750 | trend 8.400 | rang 7.514
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : PROM-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.660 | entrée 6.450 | trend 8.950 | rang 8.167
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. ALGO-EUR — ACHETE_MAINTENANT — rank 7.995 — opportunité 8.804 — entrée 6.850 — trend 8.150
2. WIF-EUR — ACHETE_MAINTENANT — rank 7.465 — opportunité 8.679 — entrée 6.950 — trend 7.150
3. PEPE-EUR — ACHETE_MAINTENANT — rank 7.136 — opportunité 8.812 — entrée 7.400 — trend 6.150
4. HYPE-EUR — ACHETE_MAINTENANT — rank 6.293 — opportunité 7.384 — entrée 7.400 — trend 5.150

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. PROM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.167
2. WOO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.163
3. ZRO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.034

## Accélération indépendante

- ACE-EUR — CONFIRMED_ACCELERATION — score 8.405/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- OSMO-EUR — CONFIRMED_ACCELERATION — score 8.342/10 — DETECTED_BUT_TOO_LATE
- CAP-EUR — CONFIRMED_ACCELERATION — score 7.019/10 — DETECTED_BUT_TOO_LATE
- EPIC-EUR — CONFIRMED_ACCELERATION — score 6.790/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MOVR-EUR — CONFIRMED_ACCELERATION — score 6.702/10 — DETECTED_BUT_TOO_LATE
- PROMPT-EUR — CONFIRMED_ACCELERATION — score 6.667/10 — DETECTED_BUT_TOO_LATE
- SAFE-EUR — BUILDING_ACCELERATION — score 5.360/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- XYO-EUR — MEMORY_24H — score mémoire 9.473/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- HEI-EUR — MEMORY_24H — score mémoire 9.300/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ARPA-EUR — MEMORY_24H — score mémoire 8.595/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 8.568/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SWEAT-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TAI-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ACE-EUR — ACTIVE_NOW — score mémoire 8.405/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- OSMO-EUR — ACTIVE_NOW — score mémoire 8.342/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- VELO-EUR — MEMORY_24H — score mémoire 8.181/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- SWEAT-EUR +214.08% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- MOVR-EUR +82.67% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NOM-EUR +35.72% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CT-EUR +31.17% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CAP-EUR +21.60% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- MON-EUR +20.71% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- STX-EUR +16.82% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VELO-EUR +16.43% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- NOS-EUR +13.92% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- JASMY-EUR +13.22% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
