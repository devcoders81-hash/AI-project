interface Props {
    sequence: number;
    total: number;
}

export default function InterviewHeader({
    sequence,
    total,
}: Props) {

    const percentage = (sequence / total) * 100;

    return (

        <div className="bg-white rounded-xl shadow p-6 mb-6">

            <div className="flex justify-between">

                <h2 className="text-2xl font-bold">
                    AI Mock Interview
                </h2>

                <span>
                    Question {sequence} / {total}
                </span>

            </div>

            <div className="w-full bg-gray-200 rounded mt-4 h-3">

                <div
                    className="bg-blue-600 h-3 rounded"
                    style={{
                        width: `${percentage}%`
                    }}
                />

            </div>

        </div>

    );

}