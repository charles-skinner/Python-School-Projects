def main():
    annualReports = {}
    monthReports = {}
    for year in range(1994,2013):
        annualReports[year] = []
        monthReports[year] = [[],[],[],[],[],[],[],[],[],[],[],[]]
    with open("gas_prices.txt") as f:
        data = f.readlines()
    for line in data:
        annualReports[int(line[6:10])].append(float(line[11:]))
        monthReports[int(line[6:10])][int(line[0:2])-1].append(float(line[11:]))
    with open("gas_report.txt","w") as f:
        for year in range(1994,2013):
            low = "{:.2f}".format(min(annualReports[year]))
            avg = "{:.2f}".format(sum(annualReports[year])/len(annualReports[year]))
            high = "{:.2f}".format(max(annualReports[year]))
            jan = "{:.2f}".format(sum(monthReports[year][0])/len(monthReports[year][0]))
            feb = "{:.2f}".format(sum(monthReports[year][1])/len(monthReports[year][1]))
            mar = "{:.2f}".format(sum(monthReports[year][2])/len(monthReports[year][2]))
            apr = "{:.2f}".format(sum(monthReports[year][3])/len(monthReports[year][3]))
            may = "{:.2f}".format(sum(monthReports[year][4])/len(monthReports[year][4]))
            jun = "{:.2f}".format(sum(monthReports[year][5])/len(monthReports[year][5]))
            jul = "{:.2f}".format(sum(monthReports[year][6])/len(monthReports[year][6]))
            aug = "{:.2f}".format(sum(monthReports[year][7])/len(monthReports[year][7]))
            sep = "{:.2f}".format(sum(monthReports[year][8])/len(monthReports[year][8]))
            oct = "{:.2f}".format(sum(monthReports[year][9])/len(monthReports[year][9]))
            nov = "{:.2f}".format(sum(monthReports[year][10])/len(monthReports[year][10]))
            dec = "{:.2f}".format(sum(monthReports[year][11])/len(monthReports[year][11]))        
            f.writelines(f"{year}:\n")
            f.write(f"\tLow: ${low}, Avg: ${avg}, High: ${high}\n")
            f.write(f"\tJanuary    ${jan}\n")
            f.write(f"\tFebruary   ${feb}\n")
            f.write(f"\tMarch      ${mar}\n")
            f.write(f"\tApril      ${apr}\n")
            f.write(f"\tMay        ${may}\n")
            f.write(f"\tJune       ${jun}\n")
            f.write(f"\tJuly       ${jul}\n")
            f.write(f"\tAugust     ${aug}\n")
            f.write(f"\tSeptember  ${sep}\n")
            f.write(f"\tOctober    ${oct}\n")
            f.write(f"\tNovember   ${nov}\n")
            f.write(f"\tDecember   ${dec}\n")
            f.write("\n")

if __name__ == "__main__":
    main()