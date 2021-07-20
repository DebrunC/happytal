import pandas as pd
from core.config import settings

def getRecommendationByClient(user_id,numReco):
    neighbors = []
    recommendations = []
    userToProduct = pd.read_csv(settings.USER_TO_PRODUCT)
    similarity_matrix_df = pd.read_csv(settings.SIMILARITY_MATRIX,index_col=0)

    if (user_id not in userToProduct['User_ID'].values):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="user email not found")


    #for each product of the user find the 5 more similar products
    for index, row in userToProduct[userToProduct['User_ID']==user_id].iterrows():
        prod=row['product_id']
        rating=row["product_rating"]        
    
        s=list(zip(similarity_matrix_df.loc[prod,:].index,similarity_matrix_df.loc[prod,:]*rating))
        s_sorted = sorted(s, key=lambda x: x[1], reverse=True)[1:numReco+1]
        neighbors.extend(s_sorted)
    # the 5 more similar products of the user 
    numberAdded = 0
    neighbors = sorted(neighbors, key=lambda x: x[1], reverse=True) 
    i=0
    while (numberAdded<numReco) or (i<len(neighbors)):
        if neighbors[i][0] not in recommendations:
            recommendations.append(neighbors[i][0])
            numberAdded=numberAdded+1
        i=i+1
    return {"recommendations":recommendations,"Number of recommendations": numReco}