# Source indépendante de capitalisation (SHADOW OGN/RLC/ZRC)

**Règle : aucune modification production, aucun ordre, aucun email, aucun veto ajouté.**

Pour débloquer le shadow volume/cap (#134), les correspondances ont été contrôlées sur les pages CoinGecko :
- `OGN-EUR` → <https://www.coingecko.com/en/coins/origin-protocol> (`origin-protocol`) ;
- `RLC-EUR` → <https://www.coingecko.com/en/coins/iexec-rlc> (`iexec-rlc`) ;
- `ZRC-EUR` → <https://www.coingecko.com/en/coins/zircuit> (`zircuit`).

Le script `scripts/scan_verified_cap_probe.py` interroge **en premier** l'API CoinGecko `/coins/markets?vs_currency=eur` pour récupérer `market_cap`, `total_volume`, `current_price`, `last_updated`; il interroge **ensuite** l'API publique Bitvavo `/ticker/24h` pour `volumeQuote`, `timestamp`, `last`, `bid`, `ask`, conformément à <https://docs.bitvavo.com/docs/rest-api/get-ticker-data-24-h/>.

Le fournisseur doit identifier `id` et `symbol` attendus. Une divergence de prix supérieure à 20% fait échouer la vérification d'identité, un market-cap futur par rapport à l'horodatage Bitvavo est rejeté et un market-cap de plus de deux heures est périmé. Les sources n'exposent aucun compte privé. Une panne HTTP se voit comme un **échec de collecte**, jamais comme une absence d'opportunité.

Le résultat expose séparément :
- `turnover_global_24h_pct = 100 * total_volume_coingecko_eur / market_cap_coingecko_eur` (même fournisseur).
- `turnover_bitvavo_24h_pct = 100 * volumeQuote_bitvavo_eur / market_cap_coingecko_eur` (volume local plateforme).
- `spread_pct` du ticker, **sans** prétendre mesurer le slippage d'un ordre de 150 €.
- `cap_coverage_pct` et toutes les omissions avec leur motif.
- `volume_last_1h_vs_prev_1h` reste indisponible dans cet observateur ponctuel : il est mesuré **séparément** par `bitvavo_live.json`, avec son propre timestamp ; les deux ne sont pas fusionnés fictivement.

La CI teste des données simulées dans les PR, puis observe les **trois actifs** en mode non trader sur fusion et toutes les **six heures** ; le résultat horodaté est conservé en artefact GitHub Actions durant 30 jours.

## État des preuves

Ce lancement sert à **prouver la collecte ex ante** et la cohérence des ratios, pas à prétendre que ces trois hausses étaient prévisibles. L'ajout d'autres actifs à la table d'identité devra être revu avant d'augmenter la couverture. La comparaison prospective complète de gain net avec/sans ratio nécessite les futurs horizons maturés, une gestion des sorties identique, des perdants autant que des gagnants et une mesure réaliste du carnet.

Ne jamais extrapoler un ratio élevé en conseil d'achat. Le seuil `20%` n'est qu'un contrôle conservateur de cohérence des prix inter-plateformes pour éviter un mauvais token, **pas** un seuil de stratégie.
