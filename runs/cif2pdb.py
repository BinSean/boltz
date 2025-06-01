cifPath = './output/boltz_results_ligand/predictions/ligand/ligand_model_0.cif'

# f = open(cifPath)
# print(f.read())

import gemmi

# 用 gemmi 先读取 cif 文件 再输出 pdb文件
st = gemmi.read_structure(cifPath, format=gemmi.CoorFormat.Mmcif)

st.write_pdb('./output/kkkkkk.pdb')
print('done')


