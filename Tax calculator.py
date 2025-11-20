# uk_tax_calculator_v2.py

PERSONAL_ALLOWANCE = 12570  # 2025/26 standard personal allowance


def calc_england_wales_tax(income: float) -> dict:
    """
    England & Wales income tax 2025/26.
    Taxable income bands:
      - 20% on first £37,700
      - 40% on next £74,870 (to £112,570)
      - 45% above £112,570
    """
    taxable = max(0.0, income - PERSONAL_ALLOWANCE)

    basic_band = min(taxable, 37700)
    higher_band = max(min(taxable - 37700, 74870), 0)
    additional_band = max(taxable - 112570, 0)

    tax_20 = basic_band * 0.20
    tax_40 = higher_band * 0.40
    tax_45 = additional_band * 0.45

    total_tax = tax_20 + tax_40 + tax_45

    return {
        "region": "England/Wales",
        "taxable_income": taxable,
        "tax_20": tax_20,
        "tax_40": tax_40,
        "tax_45": tax_45,
        "total_tax": total_tax,
    }


def calc_scotland_tax(income: float) -> dict:
    """
    Scotland income tax 2025/26.
    Taxable income bands:
      - Starter 19%:      0 – 2,827
      - Basic 20%:        2,828 – 14,921
      - Intermediate 21%: 14,922 – 31,092
      - Higher 42%:       31,093 – 62,430
      - Advanced 45%:     62,431 – 125,140
      - Top 48%:          125,141+
    """
    taxable = max(0.0, income - PERSONAL_ALLOWANCE)

    # helper for “slice” of taxable income
    def band_amount(t, lower, upper=None):
        if upper is None:
            return max(t - lower, 0)
        return max(min(t, upper) - lower, 0)

    starter = band_amount(taxable, 0, 2827)
    basic = band_amount(taxable, 2827, 14921)
    intermediate = band_amount(taxable, 14921, 31092)
    higher = band_amount(taxable, 31092, 62430)
    advanced = band_amount(taxable, 62430, 125140)
    top = band_amount(taxable, 125140, None)

    tax_starter = starter * 0.19
    tax_basic = basic * 0.20
    tax_intermediate = intermediate * 0.21
    tax_higher = higher * 0.42
    tax_advanced = advanced * 0.45
    tax_top = top * 0.48

    total_tax = (
        tax_starter
        + tax_basic
        + tax_intermediate
        + tax_higher
        + tax_advanced
        + tax_top
    )

    return {
        "region": "Scotland",
        "taxable_income": taxable,
        "starter": tax_starter,
        "basic": tax_basic,
        "intermediate": tax_intermediate,
        "higher": tax_higher,
        "advanced": tax_advanced,
        "top": tax_top,
        "total_tax": total_tax,
    }


def main():
    print("UK Income Tax Calculator 2025/26")
    print("--------------------------------\n")

    nationality = input("Enter your nationality: ").strip()
    income_str = input("Enter your annual income in £ (numbers only): ").strip()

    try:
        income = float(income_str)
    except ValueError:
        print("Income must be a number. Exiting.")
        return

    print("\nWhich tax system applies to you?")
    print("  1 - England/Wales")
    print("  2 - Scotland")
    choice = input("Enter 1 or 2: ").strip()

    if choice == "2":
        result = calc_scotland_tax(income)
    else:
        result = calc_england_wales_tax(income)

    region = result["region"]
    taxable = result["taxable_income"]
    effective_rate = (result["total_tax"] / income) * 100 if income > 0 else 0.0

    print("\n----- TAX SUMMARY -----")
    print(f"Nationality:       {nationality}")
    print(f"Region for tax:    {region}")
    print(f"Annual income:     £{income:,.2f}")
    print(f"Personal allowance £{PERSONAL_ALLOWANCE:,.2f}")
    print(f"Taxable income:    £{taxable:,.2f}\n")

    if region == "England/Wales":
        print("Breakdown (England & Wales bands):")
        print(f"  20% band tax:    £{result['tax_20']:,.2f}")
        print(f"  40% band tax:    £{result['tax_40']:,.2f}")
        print(f"  45% band tax:    £{result['tax_45']:,.2f}")
    else:
        print("Breakdown (Scottish bands):")
        print(f"  Starter 19%:     £{result['starter']:,.2f}")
        print(f"  Basic 20%:       £{result['basic']:,.2f}")
        print(f"  Intermediate 21%:£{result['intermediate']:,.2f}")
        print(f"  Higher 42%:      £{result['higher']:,.2f}")
        print(f"  Advanced 45%:    £{result['advanced']:,.2f}")
        print(f"  Top 48%:         £{result['top']:,.2f}")

    print("\nTOTAL TAX:")
    print(f"  Annual tax due:  £{result['total_tax']:,.2f}")
    print(f"  Effective rate:  {effective_rate:.2f}% of your income")


if __name__ == "__main__":
    main()
