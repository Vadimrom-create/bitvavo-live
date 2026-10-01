# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-01T13:52:08.775146+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AAVE-EUR | action ACHETE_MAINTENANT | opportunité 8.420 | entrée 6.850 | trend 8.700 | rang 8.067
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : RED-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.553 | entrée 5.800 | trend 8.950 | rang 8.042
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : KSM-EUR | action LATENT_ACCELERATOR | opportunité 7.899 | entrée 5.750 | trend 8.950 | rang 7.774
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : PROM-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.985 | entrée 6.450 | trend 8.950 | rang 7.909
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. AAVE-EUR — ACHETE_MAINTENANT — rank 8.067 — opportunité 8.420 — entrée 6.850 — trend 8.700
2. ZIG-EUR — ACHETE_MAINTENANT — rank 7.933 — opportunité 8.115 — entrée 6.950 — trend 8.750
3. WIF-EUR — ACHETE_MAINTENANT — rank 7.168 — opportunité 8.001 — entrée 7.000 — trend 7.150

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. AAVE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.067
2. RED-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 8.042
3. ZIG-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.933

## Accélération indépendante

- TREAD-EUR — CONFIRMED_ACCELERATION — score 6.937/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SYN-EUR — CONFIRMED_ACCELERATION — score 6.697/10 — DETECTED_BUT_TOO_LATE
- SWEAT-EUR — CONFIRMED_ACCELERATION — score 6.511/10 — DETECTED_BUT_TOO_LATE
- KAIA-EUR — BUILDING_ACCELERATION — score 6.216/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HFT-EUR — BUILDING_ACCELERATION — score 5.820/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FLOKI-EUR — BUILDING_ACCELERATION — score 5.397/10 — DETECTED_BUT_TOO_LATE
- WIF-EUR — BUILDING_ACCELERATION — score 5.372/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ALGO-EUR — BUILDING_ACCELERATION — score 4.969/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AERO-EUR — BUILDING_ACCELERATION — score 4.904/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- CPOOL-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XYO-EUR — MEMORY_24H — score mémoire 9.473/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CT-EUR — MEMORY_24H — score mémoire 8.691/10 — sources ACCELERATION — MEMORY_ONLY
- ARPA-EUR — MEMORY_24H — score mémoire 8.595/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 8.568/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TAI-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ACE-EUR — MEMORY_24H — score mémoire 8.405/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- OSMO-EUR — MEMORY_24H — score mémoire 8.342/10 — sources ACCELERATION — MEMORY_ONLY
- VELO-EUR — MEMORY_24H — score mémoire 8.181/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- SWEAT-EUR +142.32% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- MOVR-EUR +77.75% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CT-EUR +43.36% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CAP-EUR +24.15% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- MON-EUR +16.24% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- STX-EUR +15.02% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VELO-EUR +14.58% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- HEI-EUR +13.86% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SYN-EUR +13.47% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NOM-EUR +13.46% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
