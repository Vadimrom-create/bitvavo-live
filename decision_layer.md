# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-02T04:25:51.516202+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AAVE-EUR | action ACHETE_MAINTENANT | opportunité 8.690 | entrée 7.750 | trend 8.950 | rang 8.254
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : SKY-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.518 | entrée 6.450 | trend 8.000 | rang 7.251
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : HUMA-EUR | action LATENT_ACCELERATOR | opportunité 8.050 | entrée 5.050 | trend 8.850 | rang 7.684
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : STX-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.615 | entrée 6.900 | trend 8.650 | rang 8.108
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. AAVE-EUR — ACHETE_MAINTENANT — rank 8.254 — opportunité 8.690 — entrée 7.750 — trend 8.950
2. LINK-EUR — ACHETE_MAINTENANT — rank 7.437 — opportunité 8.662 — entrée 7.650 — trend 6.450
3. SOL-EUR — ACHETE_MAINTENANT — rank 7.436 — opportunité 8.810 — entrée 7.850 — trend 6.350
4. AVAX-EUR — ACHETE_MAINTENANT — rank 7.416 — opportunité 8.679 — entrée 7.650 — trend 6.650
5. PUMP-EUR — ACHETE_MAINTENANT — rank 7.397 — opportunité 8.201 — entrée 7.200 — trend 7.800
6. PEPE-EUR — ACHETE_MAINTENANT — rank 7.316 — opportunité 8.812 — entrée 7.650 — trend 6.150
7. ADA-EUR — ACHETE_MAINTENANT — rank 7.307 — opportunité 8.362 — entrée 7.450 — trend 6.600
8. FET-EUR — ACHETE_MAINTENANT — rank 7.280 — opportunité 8.224 — entrée 7.650 — trend 6.800
9. TAO-EUR — ACHETE_MAINTENANT — rank 7.184 — opportunité 8.063 — entrée 7.400 — trend 6.550
10. UNI-EUR — ACHETE_MAINTENANT — rank 7.125 — opportunité 8.743 — entrée 7.650 — trend 5.850
11. DOGE-EUR — ACHETE_MAINTENANT — rank 6.956 — opportunité 8.623 — entrée 7.500 — trend 5.600
12. WIF-EUR — ACHETE_MAINTENANT — rank 6.879 — opportunité 8.796 — entrée 7.000 — trend 6.250
13. GRAM-EUR — ACHETE_MAINTENANT — rank 6.746 — opportunité 7.453 — entrée 6.800 — trend 6.300
14. XRP-EUR — ACHETE_MAINTENANT — rank 6.734 — opportunité 8.477 — entrée 7.700 — trend 4.900
15. SHIB-EUR — ACHETE_MAINTENANT — rank 6.522 — opportunité 8.117 — entrée 7.200 — trend 5.050

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. AAVE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.254
2. STX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.108
3. HUMA-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.684

## Accélération indépendante

- HFT-EUR — CONFIRMED_ACCELERATION — score 8.078/10 — DETECTED_BUT_TOO_LATE
- SCR-EUR — CONFIRMED_ACCELERATION — score 7.727/10 — DETECTED_BUT_TOO_LATE
- TIA-EUR — CONFIRMED_ACCELERATION — score 6.713/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ILV-EUR — BUILDING_ACCELERATION — score 6.454/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZK-EUR — BUILDING_ACCELERATION — score 6.331/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DOT-EUR — BUILDING_ACCELERATION — score 5.691/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- USELESS-EUR — BUILDING_ACCELERATION — score 5.452/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WCT-EUR — BUILDING_ACCELERATION — score 5.304/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- QNT-EUR — BUILDING_ACCELERATION — score 5.045/10 — DETECTED_BUT_TOO_LATE
- LPT-EUR — BUILDING_ACCELERATION — score 4.995/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- CPOOL-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.847/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- OSMO-EUR — MEMORY_24H — score mémoire 8.342/10 — sources ACCELERATION — MEMORY_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.254/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AGI-EUR — MEMORY_24H — score mémoire 8.119/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- STX-EUR — ACTIVE_NOW — score mémoire 8.108/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HFT-EUR — ACTIVE_NOW — score mémoire 8.078/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- U-EUR — MEMORY_24H — score mémoire 8.002/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SCR-EUR — ACTIVE_NOW — score mémoire 7.727/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- HUMA-EUR — ACTIVE_NOW — score mémoire 7.684/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SWEAT-EUR +127.76% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- GTC-EUR +57.14% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SCR-EUR +48.79% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CT-EUR +27.46% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MEGA-EUR +20.85% — DETECTED_EARLY — couche NONE — action NONE
- SYN-EUR +18.13% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SUPER-EUR +16.41% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ALICE-EUR +15.31% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MOVR-EUR +13.30% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NOS-EUR +13.27% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
