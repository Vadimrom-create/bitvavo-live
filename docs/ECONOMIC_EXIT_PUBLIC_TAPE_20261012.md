# Solaire — audit des volumes réellement négociés autour des sorties théoriques (12 octobre 2026)

**Statut : mesure indépendante de recherche, issue #134 et PR #163 (non fusionnée).**

## Objectif et provenance

Auditer l'**activité publique** autour des 29 sorties modélisées du scénario « dernier prix » et des 28 sorties du scénario « premier prix négocié ». Après dédoublonnage marché+créneau : **44 fenêtres de dix minutes**, sur **22 marchés**, correspondant au même jeu de **75 alertes BUY_SENT / 44 marchés suivis** figé le 11 octobre.

Source stricte de la cohorte : `scripts/audit_frozen_exit_execution.py` et son artifact [#11713430176](https://github.com/Vadimrom-create/bitvavo-live/actions/runs/38168762021), SHA-256 bougies `6df783e699ae28ae63d791223000c4c5f11e1a660025521093154fba98b557d6`.

Contrôle public effectué le **12 octobre** avec `GET /v2/{market}/trades`, période de 10 minutes par sortie et au plus 1 000 transactions par requête. Chaque réponse complète, avec transactions publiques, horodatages et empreinte SHA-256, se trouve dans l'artifact [run 38285246349](https://github.com/Vadimrom-create/bitvavo-live/actions/runs/38285246349). **Ne jamais associer ces transactions à l'utilisateur.**

Sources officielles :
- https://docs.bitvavo.com/docs/rest-api/get-trades/
- https://docs.bitvavo.com/docs/rest-api/get-order-book/
- https://docs.bitvavo.com/docs/rest-api/get-candlestick-data/

## Résultats des 44 fenêtres figées

| Indicateur d'activité publique | Fenêtres / 44 |
|--|--:|
| Récupération complète, sans erreur ni limite de 1 000 atteinte | 44 |
| Zéro transaction durant les 5 min de la bougie de sortie | **6** |
| Moins de 100 EUR négociés dans ces 5 min (zéros compris) | **11** |
| Zéro transaction dans les 5 min suivant la sortie théorique | **14** |
| Moins de 100 EUR négociés dans les 5 min suivant la sortie | **20** |
| Carnets **historiques** de sortie retrouvés | **0** |
| **Ventes réelles de l'utilisateur** vérifiées | **0** |

Six fenêtres avec **aucun échange** pendant la bougie qui servait à valoriser la vente « horizon 24h » : **ARPA, BEL, CC, EDU, HEI, W**. Cela confirme empiriquement l'un des risques du prolongement du dernier prix. Cette liste n'est pas un classement d'actifs ; elle décrit seulement ces dates de sortie.

**Limite causale :** le volume échangé par d'autres personnes n'est PAS la profondeur des ordres d'achat en attente. Un flux inférieur à 100 EUR ne signifie pas qu'une vente hypothétique de 100 EUR était impossible ; même un flux supérieur à 100 EUR ne démontre pas qu'elle aurait été réalisée au prix utilisé. L'API publique des transactions ne contient pas de carnet historique exécutable ni d'ordres personnels.

## Sensibilité aux coûts de sortie — allocations figées, PAS nouveau backtest

En gardant *exactement les mêmes sorties/positions papier* et en appliquant une décote supplémentaire à leurs produits de vente supposés, sans réallocation chronologique, nous obtenons :

| Décote additionnelle sur les produits de vente | Modèle dernier prix (29) | Modèle première transaction (28) |
|--|--:|--:|
| Aucune, coûts déjà supposés inclus | −7,49 EUR | −2,71 EUR |
| 0,25 % supplémentaire | −14,72 EUR | −9,70 EUR |
| 0,5 % supplémentaire | −21,95 EUR | −16,70 EUR |
| 1 % supplémentaire | −36,42 EUR | −30,68 EUR |
| 2 % supplémentaire | −65,34 EUR | −58,66 EUR |

Ces décotes sont des **scénarios**, pas une mesure des vrais écarts de prix. Elles sont appliquées à des flux déjà réduits de frais 0,25 % et de glissement adverse 0,10 % par côté. L'immobilisation de capital n'est pas recalculée si les coûts changent : il s'agit d'une dérivée de sensibilité, pas d'une nouvelle stratégie ou d'un PnL réalisable.

## Conclusions et prochain verrou

1. La source `/candles` fournit officiellement **OHLCV** mais le premier collecteur a omis le volume ; ce contrôle par `/trades` corrige partiellement ce manque **sans rétrocréer les volumes manquants**.
2. **STOP/GO = aucun GO trading réel**. La rentabilité réellement exécutable, les fills, les bid/ask et le drawdown liquidable restent non identifiables.
3. Pour obtenir des comparaisons V4/R2/témoin : figer prospectivement des horodatages communs et les **carnets de sortie au même moment** (profondeur 100–150 EUR, latence, écarts, annulations) dans un dispositif purement shadow. Aucun raccordement aux ordres/clé privée de Bitvavo n'est requis pour cette première étape.
4. Les archives GitHub de résultats de recherche expirent après 14 jours ; conserver séparément les preuves d'entrée, sorties et bandes publiques. Ne pas pousser d'éléments de portefeuille privé dans GitHub public.

Aucun changement du scanner de production, des stops, BUY, seuils ou ordres n'a été effectué.
