import matplotlib.pyplot as plt


def moving_average(data, window_size):
    moving_averages = []
    for i in range(window_size, len(data) + 1):
        window = data[i - window_size:i]
        average = sum(window) / window_size
        moving_averages.append(average)
    return moving_averages


# dictionary = {'allendennis': 600.0, 'amandahanson': 205.57553956834724, 'annette23': 278.9568345323761, 'annpeterson': 289.7482014388495, 'austintran': 460.25179856115517, 'awillis': 352.338129496405, 'barkerrandy': 356.1151079136735, 'bowmanjane': 185.07194244604156, 'brianmeadows': 564.9280575539515, 'brittany85': 587.5899280575491, 'bruce17': 384.7122302158293, 'caleb23': 257.374100719422, 'carmenjones': 162.41007194244597, 'chasejennings': 662.5899280575512, 'christina01': 432.19424460431816, 'christopher32': 550.3597122302161, 'cscott': 87.41007194244595, 'danagardner': 53.95683453237424, 'davilalisa': 485.6115107913718, 'deborah90': 248.74100719424337, 'donna51': 183.9928057553955, 'dylanhudson': 198.0215827338116, 'eelliott': 159.71223021582557, 'elizabeth06': 199.64028776978378, 'eric90': 226.0791366906485, 'estewart': 290.82733812949635, 'fallen': 216.36690647482126, 'fbautista': 514.2086330935197, 'fmorris': 463.4892086330882, 'gallagherpatrick': 365.28776978417113, 'garciashaun': 544.424460431651, 'garrettestrada': 439.74820143884523, 'gina72': 566.0071942445993, 'hbray': 146.22302158273442, 'henry37': 450.0, 'herrerasusan': 541.1870503597086, 'hmarquez': 317.80575539568423, 'humphreyjacob': 393.88489208632626, 'istewart': 396.0431654676232, 'james70': 451.6187050359727, 'jday': 501.25899280575675, 'johnsonalex': 492.62589928057287, 'justin87': 300.0, 'karenlewis': 339.9280575539556, 'kathleenboyd': 341.5467625899272, 'kelly33': 533.6330935251841, 'kevinjacobson': 408.45323741007434, 'kimberlyhunter': 379.3165467625929, 'kimberlyphillips': 346.9424460431626, 'kjones': 426.7985611510808, 'kristajuarez': 217.98561151079343, 'lindamiddleton': 397.6618705035949, 'lisamclean': 750.0, 'lorigeorge': 603.7769784172656, 'martinezbeverly': 532.014388489211, 'matthewmiller': 362.58992805754997, 'mcarpenter': 582.7338129496413, 'melissa56': 641.0071942445987, 'mglenn': 590.2877697841674, 'michaelwilliams': 387.41007194245066, 'mjones': 445.1438848920827, 'moralesamanda': 370.68345323740715, 'murphyadriana': 523.9208633093514, 'njohnson': 563.3093525179808, 'nshepherd': 286.51079136690674, 'oadams': 551.9784172661875, 'osalazar': 588.6690647481978, 'parkerstafford': 459.1726618705075, 'rclark': 323.20143884891934, 'reidchase': 304.85611510791637, 'reynoldsmarcus': 310.25179856115136, 'richard49': 410.07194244604614, 'richmondmonica': 161.3309352517975, 'rjohnston': 154.85611510791352, 'robersonjessica': 212.58992805755403, 'robertjarvis': 457.0143884892105, 'rvalencia': 298.3812949640275, 'samanthahenry': 537.4100719424526, 'scottmaria': 208.81294964028697, 'sheila84': 108.99280575539672, 'spratt': 339.3884892086314, 'steven42': 365.82733812949414, 'sydneyphillips': 410.6115107913704, 'theresacortez': 471.0431654676229, 'tim01': 384.1726618705062, 'valenciacynthia': 150.0, 'vasquezkevin': 292.98561151079303, 'vaughnkristina': 595.1438848920857, 'vhodges': 186.6906474820137, 'vramirez': 0.0, 'wandabrooks': 167.26618705035992, 'warewendy': 336.6906474820168, 'webbstacey': 264.3884892086345, 'wgallagher': 696.0431654676224, 'ybowman': 235.7913669064736, 'ycurtis': 353.95683453237655, 'zgibson': 413.30935251798115, 'zspence': 403.0575539568375}
# data = list(dictionary.values())
data = [52.459896557312675, 53.25004311619772, 54.92007747892872, 55.10437259562655, 55.483986559160186]
window_size = 2

# Calculate moving average
moving_averages = moving_average(data, window_size)

# Plotting the original data
plt.plot(data, label='Original Data')

# Plotting the moving average
plt.plot(range(window_size - 1, len(data)), moving_averages, label='Moving Average')

plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.show()
