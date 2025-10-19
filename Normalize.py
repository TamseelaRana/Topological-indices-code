# Normalized Triangular MFs Code 

# Load the values of Topological indices
M1 = np.array([312, 252, 458, 400, 376, 458, 324, 280, 190, 372, 286, 232, 290, 214, 256, 278, 400, 352, 212, 362])

M1_norm = (M1 - M1.min()) / (M1.max() - M1.min())

x_min = M1_norm.min()
x_max = M1_norm.max()
x_mid = M1_norm.mean()

low_mf = fuzz.trimf(M1_norm, [x_min, x_min, x_mid])
med_mf = fuzz.trimf(M1_norm, [x_min, x_mid, x_max])
high_mf = fuzz.trimf(M1_norm, [x_mid, x_max, x_max])

df = pd.DataFrame({
    'M1_Original': M1,
    'M1_Normalized': M1_norm.round(4),
    'Low_Membership': low_mf.round(4),
    'Medium_Membership': med_mf.round(4),
    'High_Membership': high_mf.round(4)
})

print(df.to_string(index=False))

